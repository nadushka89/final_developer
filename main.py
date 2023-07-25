from model.AnimalRegistry import AnimalRegistry
from presenter.AnimalPresenter import AnimalPresenter
from view.AnimalView import AnimalView


if __name__ == "__main__":
    view = AnimalView()
    model=AnimalRegistry()
    presenter=AnimalPresenter(view,model)
    presenter.run()