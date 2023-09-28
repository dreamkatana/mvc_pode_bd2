from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.loja import ModeloLoja
from schemas import EsquemaLoja


blp = Blueprint("Lojas", "lojas", description="Operações em lojas")


@blp.route("/loja/<string:id_loja>")
class Loja(MethodView):
    @blp.response(200, EsquemaLoja)
    def get(self, id_loja):
        loja = ModeloLoja.query.get_or_404(id_loja)
        return loja

    def delete(self, id_loja):
        loja = ModeloLoja.query.get_or_404(id_loja)
        db.session.delete(loja)
        db.session.commit()
        return {"message": "Loja deletada"}, 200


@blp.route("/loja")
class ListaLoja(MethodView):
    @blp.response(200, EsquemaLoja(many=True))
    def get(self):
        return ModeloLoja.query.all()

    @blp.arguments(EsquemaLoja)
    @blp.response(201, EsquemaLoja)
    def post(self, dados_loja):
        loja = ModeloLoja(**dados_loja)
        try:
            db.session.add(loja)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="Uma loja com esse nome já existe.",
            )
        except SQLAlchemyError:
            abort(500, message="Ocorreu um erro ao criar a loja.")

        return loja
