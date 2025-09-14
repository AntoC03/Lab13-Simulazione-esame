import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.view = view
        # the model, which implements the logic of the program and holds the data
        self.model = model

    def handleDDYearSelection(self, e):
        pass

    def handleCreaGrafo(self,e):
        self.view.txt_result.clean()
        self.view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato:"))
        self.view.txt_result.controls.append(ft.Text(f"Numero di nodi: {self.model.get_grafo(self.view._ddAnno.value)}"))
        self.view.txt_result.controls.append(ft.Text(f"Numero di archi: {self.model.get_archi()}"))
        self.view.txt_result.controls.append(ft.Text(f"Best driver: {self.model.miglior_pilota()[0].surname}, with score {self.model.miglior_pilota()[1]}"))
        self.view.update_page()


    def handleCerca(self, e):
        pass

    def fillDDYear(self):
        for i in self.model.get_anni():
            self.view._ddAnno.options.append(ft.dropdown.Option(key=i, text=i))
        self.view.update_page()