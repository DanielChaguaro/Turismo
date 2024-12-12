from flask import session, render_template , request
from app.models.Actividad import Actividad
from app.models.db import db
from app.models.Usuario import Usuario
from app.models.Reserva import Reserva
from app.models.Destino import Destino
from sqlalchemy import func,text
from datetime import datetime

def recomendaciones_basicas():
        usuario_id = session.get('user_id')
        if not usuario_id:
            return "Usuario no autenticado."
        usuario = Usuario.query.get(usuario_id)
        preferencias = usuario.preferencias.split(',') if usuario.preferencias else []
        actividades = Actividad.query.all()
        fecha_inicial = request.form.get('fecha_inicial')
        fecha_final = request.form.get('fecha_final')
        
        if fecha_inicial:
            fecha_inicial = datetime.strptime(fecha_inicial, "%Y-%m-%d")
        else:
            fecha_inicial = datetime.strptime('2000-01-01', "%Y-%m-%d")

        if fecha_final:
            fecha_final = datetime.strptime(fecha_final, "%Y-%m-%d")
        else:
            fecha_final =  datetime.strptime('2025-12-31', "%Y-%m-%d")
        temporada_actual = None
        if fecha_inicial:
            mes_inicial = fecha_inicial.month
            if mes_inicial in [12, 1, 2]:
                temporada_actual = "invierno"
            elif mes_inicial in [3, 4, 5]:
                temporada_actual = "primavera"
            elif mes_inicial in [6, 7, 8]:
                temporada_actual = "verano"
            else:
                temporada_actual = "otoño"    
        historial = usuario.historial
        reservas_por_actividad = (
            db.session.query(Reserva.actividad_id, func.count(Reserva.id).label("total_reservas"))
            .filter(Reserva.fecha >= fecha_inicial)
            .filter(Reserva.fecha <= fecha_final)
            .group_by(Reserva.actividad_id)
            .all()
        )
        reservas_dict = {reserva.actividad_id: reserva.total_reservas for reserva in reservas_por_actividad}
        max_reservas = max(reservas_dict.values(), default=1)
        min_precio = min([actividad.precio for actividad in Actividad.query.all()], default=1)
        recomendaciones = []
        actividades_agregadas = set() 
        for preferencia in preferencias:
            for actividad in actividades:
                for destino in Destino.query.all():
                    if actividad.destino_id == destino.id:
                        if preferencia.lower() in actividad.descripcion.lower():
                            #actividad.id not in historial
                            if  actividad.id not in actividades_agregadas:
                                temporada_match = 1 if temporada_actual and (temporada_actual in destino.temporada_recomendada or 'todo el año' in destino.temporada_recomendada) else 0
                                puntaje = (
                                    (reservas_dict.get(actividad.id, 0) / max_reservas) * 0.3 +
                                    (min_precio / actividad.precio) * 0.5 +
                                    temporada_match * 0.2
                                )
                                recomendaciones.append({
                                    "id": actividad.id,
                                    "nombre": actividad.nombre,
                                    "descripcion": actividad.descripcion,
                                    "precio": actividad.precio,
                                    "destino_id": actividad.destino_id,
                                    "destino_nombre": actividad.destino.nombre,
                                    "destino_temporada": actividad.destino.temporada_recomendada,
                                    "total_reservas" : reservas_dict.get(actividad.id, 0),
                                    "puntaje": puntaje
                                })
                                actividades_agregadas.add(actividad.id)
        recomendaciones = sorted(recomendaciones, key=lambda x: (x["puntaje"]), reverse=True)
        return render_template('recomendaciones_basicas.html', recomendaciones=recomendaciones)
