class Middle:
    @staticmethod
    def open():
        # Realiza la importación diferida aquí
        from Vistas.R_selection import selection
        selection().open()