import customtkinter
import pandastable as pdt
from tkinter import filedialog
from main_economiza_AL import economiza_AL_scrap_to_df

customtkinter.set_default_color_theme('blue')  # Themes: 'blue' (standard), 'green', 'dark-blue'

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title('Economiza Alagoas')
        self.geometry(f'{App.WIDTH}x{App.HEIGHT}')
        self.protocol('WM_DELETE_WINDOW', self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky='nswe')

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky='nswe', padx=20, pady=20)
        
        # ============ frame_left ============


        self.dataframe = None
        self.table = None

        # configure grid layout
        self.frame_left.grid_rowconfigure(0, minsize=10)   
        self.frame_left.grid_rowconfigure(4, minsize=20)
        self.frame_left.grid_rowconfigure(5, weight=20)
        self.frame_left.grid_rowconfigure(8, weight=20)    
        self.frame_left.grid_rowconfigure(11, minsize=10)  

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text='Economiza AL',
                                              text_font=('Roboto Medium', -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.label_mode_filtro = customtkinter.CTkLabel(master=self.frame_left, text='Filtro:')
        self.label_mode_filtro.grid(row=6, column=0, pady=0, padx=20, sticky='w')

        self.optionmenu_filter = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        command=self.filter_bairros,
                                                        values=['-'])
        self.optionmenu_filter.grid(row=7, column=0, columnspan=1, pady=10, padx=20, sticky='we')

        self.button_shot = customtkinter.CTkButton(master=self.frame_left,
                                                text='Tirar Foto',
                                                command=self.scrap_by_shot)
        self.button_shot.grid(row=2, column=0, pady=10, padx=20)

        self.button_browse = customtkinter.CTkButton(master=self.frame_left,
                                                text='Escolher a Foto',
                                                command=self.scrap_by_browse)
        self.button_browse.grid(row=3, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text='Tema:')
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky='w')

        self.optionmenu_theme = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=['Light', 'Dark'],
                                                        command=self.change_appearance_mode)
        self.optionmenu_theme.grid(row=10, column=0, pady=10, padx=20, sticky='w')

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=3, rowspan=8, pady=20, padx=20, sticky='nsew')

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        # ============ frame_right ============ 

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=180,
                                            placeholder_text='Digite o código de barras')
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky='we')

        self.button_pesquisar = customtkinter.CTkButton(master=self.frame_right,
                                                text='Pesquisar',
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.scrap_by_barcode)
        self.button_pesquisar.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky='we')

        # set default values
        self.optionmenu_theme.set('Dark')
        self.optionmenu_filter.set('-')


    def filter_bairros(self, bairro):
        if self.table is not None:
            bairro = bairro.upper()
            if bairro != 'TODOS':
                self.table.updateModel(pdt.TableModel(self.dataframe[self.dataframe['Bairro'] == bairro]))
            else:
                self.table.updateModel(pdt.TableModel(self.dataframe))

    def scrap_by_barcode(self):
        barcode = self.entry.get() 
        if barcode:
            self.dataframe = economiza_AL_scrap_to_df(barcode=barcode)
            self.dataframe = self.dataframe[['Nome', 'Preço', 'Bairro', 'Estabelecimento']]

            list_optionmenu_filter = ['Todos'] + [bairro.title() for bairro in self.dataframe['Bairro'].unique()]
            self.optionmenu_filter.configure(values=list_optionmenu_filter)

            self.table = pdt.Table(self.frame_info,
                                   dataframe=self.dataframe[['Nome', 'Preço', 'Bairro', 'Estabelecimento']], 
                                   editable=False,
                                   enable_menus=False)
            self.table.show()

    def scrap_by_shot(self):
        self.dataframe = economiza_AL_scrap_to_df()
        self.dataframe = self.dataframe[['Nome', 'Preço', 'Bairro', 'Estabelecimento']]

        list_optionmenu_filter = ['Todos'] + [bairro.title() for bairro in self.dataframe['Bairro'].unique()]
        self.optionmenu_filter.configure(values=list_optionmenu_filter)

        self.table = pdt.Table(self.frame_info,
                               dataframe=self.dataframe[['Nome', 'Preço', 'Bairro', 'Estabelecimento']],
                               editable=False,
                               enable_menus=False)
        self.table.show()
    
    def scrap_by_browse(self):
        image_path = filedialog.askopenfilename(title='Escolha a Foto',
                                                filetypes=(('JPEG files', '*.jpeg'),
                                                           ('JPG files', '*.jpg'),
                                                           ('PNG files', '*.png')))
        self.dataframe = economiza_AL_scrap_to_df(image_path=image_path)
        self.dataframe = self.dataframe[['Nome', 'Preço', 'Bairro', 'Estabelecimento']]

        list_optionmenu_filter = ['Todos'] + [bairro.title() for bairro in self.dataframe['Bairro'].unique()]
        self.optionmenu_filter.configure(values=list_optionmenu_filter)

        self.table = pdt.Table(self.frame_info,
                               dataframe=self.dataframe[['Nome', 'Preço', 'Bairro', 'Estabelecimento']],
                               editable=False,
                               enable_menus=False)
        self.table.show()

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self):
        self.destroy()
    
if __name__ == '__main__':
    app = App()
    app.mainloop()