from flask import Blueprint
from app.controllers.auth_controller import login
from app.controllers.user_controller import dashboard, create_user, edit_user, delete_user
from app.controllers.des_controller import listar_destinos, create_destino, edit_destino, delete_destino
from app.controllers.activ_controller import listar_actividades, create_actividad, edit_actividad, delete_actividad
from app.controllers.res_controller import listar_reservas, create_reserva, edit_reserva, delete_reserva

routes = Blueprint('routes', __name__)

routes.add_url_rule('/', 'login', login, methods=['GET', 'POST'])

routes.add_url_rule('/dashboard', 'dashboard', dashboard)
routes.add_url_rule('/create_user', 'create_user', create_user, methods=['GET', 'POST'])
routes.add_url_rule('/edit_user/<int:user_id>', 'edit_user', edit_user, methods=['GET', 'POST'])
routes.add_url_rule('/delete_user/<int:user_id>', 'delete_user', delete_user)


routes.add_url_rule('/listar_destinos', 'listar_destinos', listar_destinos)
routes.add_url_rule('/create_destino', 'create_destino', create_destino, methods=['GET', 'POST'])
routes.add_url_rule('/edit_destino/<int:destino_id>', 'edit_destino', edit_destino, methods=['GET', 'POST'])
routes.add_url_rule('/delete_destino/<int:destino_id>', 'delete_destino', delete_destino)



routes.add_url_rule('/listar_actividades', 'listar_actividades', listar_actividades)
routes.add_url_rule('/create_actividad', 'create_actividad', create_actividad, methods=['GET', 'POST'])
routes.add_url_rule('/edit_actividad/<int:actividad_id>', 'edit_actividad', edit_actividad, methods=['GET', 'POST'])
routes.add_url_rule('/delete_actividad/<int:actividad_id>', 'delete_actividad', delete_actividad)



routes.add_url_rule('/listar_reservas', 'listar_reservas', listar_reservas)
routes.add_url_rule('/create_reserva/<int:actividad_id>', 'create_reserva', create_reserva, methods=['GET', 'POST'])
routes.add_url_rule('/edit_reserva/<int:reserva_id>', 'edit_reserva', edit_reserva, methods=['GET', 'POST'])
routes.add_url_rule('/delete_reserva/<int:reserva_id>', 'delete_reserva', delete_reserva)

from app.controllers.core_controller import recomendaciones_basicas, reportes

routes.add_url_rule('/recomendaciones_basicas', 'recomendaciones_basicas', recomendaciones_basicas,methods=['GET', 'POST'])
routes.add_url_rule('/reportes', 'reportes', reportes,methods=['GET', 'POST'])