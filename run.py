from infra.repository.atores_repository import AtoresRepository

# repo = FilmesRepository()
repo = AtoresRepository()
data = repo.select()

for ator in data:
    print(ator)
