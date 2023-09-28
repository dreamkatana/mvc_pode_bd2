from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.busca import ModeloBusca  # Assuming you have this model in models.busca
from schemas import ModeloBuscaSchema  # Assuming you have this schema in schemas

blp = Blueprint("Buscas", "buscas", description="Operações nas buscas")


@blp.route("/searches/<int:id>")
class Busca(MethodView):
    @blp.response(200, ModeloBuscaSchema)
    def get(self, id):
        busca = ModeloBusca.query.get_or_404(id)
        return busca

    def delete(self, id):
        busca = ModeloBusca.query.get_or_404(id)
        db.session.delete(busca)
        db.session.commit()
        return {"message": "Busca deletada."}

    @blp.arguments(ModeloBuscaSchema)
    @blp.response(200, ModeloBuscaSchema)
    def put(self, dados_busca, id):
        busca = ModeloBusca.query.get(id)

        if busca:
            busca.pokemon_name = dados_busca["pokemon_name"]
        else:
            busca = ModeloBusca(id=id, **dados_busca)

        db.session.add(busca)
        db.session.commit()

        return busca


@blp.route("/searches")
class ListaBusca(MethodView):
    @blp.response(200, ModeloBuscaSchema(many=True))
    def get(self):
        return ModeloBusca.query.all()

    @blp.arguments(ModeloBuscaSchema)
    @blp.response(201, ModeloBuscaSchema)
    def post(self, dados_busca):
        busca = ModeloBusca(**dados_busca)

        try:
            db.session.add(busca)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Ocorreu um erro ao inserir a busca.")

        return busca
