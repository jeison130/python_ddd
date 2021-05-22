from src.estudiantes.domain.listar import ListarEstudiantes

class ListarEstudiantesCase:
    def run(self):
        listarEstudiantes = ListarEstudiantes()
        return listarEstudiantes.run()