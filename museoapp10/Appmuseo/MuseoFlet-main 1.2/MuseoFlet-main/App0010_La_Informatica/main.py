import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "La historia de la Informática"
    page.bgcolor = "#61A707"
    page.window_width = 650
    page.window_height = 800
    
    image_width_Portada = 800
    image_height_Portada = 400
    
    img_height = 100
    img_width = 100
    border_radius = 25  # Ajusta el valor para el radio del borde

    # Audios Padres de la informática
    intro = ft.Audio(src="Intro.mp3", volume=1, balance=0)
    page.overlay.append(intro)
    
    Pascal = ft.Audio(src="Pascal.mp3", volume=1, balance=0)
    page.overlay.append(Pascal)
    
    Leibniz = ft.Audio(src="Leibniz.mp3", volume=1, balance=0)
    page.overlay.append(Leibniz)
    
    Babbage = ft.Audio(src="Babbage.mp3", volume=1, balance=0)
    page.overlay.append(Babbage)
    
    Lovelace = ft.Audio(src="Lovelace.mp3", volume=1, balance=0) 
    page.overlay.append(Lovelace)
    
    Hollerith = ft.Audio(src="Hollerith.mp3", volume=1, balance=0)
    page.overlay.append(Hollerith)
    
    Turing = ft.Audio(src="Turing.mp3", volume=1, balance=0)
    page.overlay.append(Turing)
    
    Neumann = ft.Audio(src="Neumann.mp3", volume=1, balance=0)
    page.overlay.append(Neumann)
    
    Shannon = ft.Audio(src="shannon.mp3", volume=1, balance=0)
    page.overlay.append(Shannon)
    
    Hopper = ft.Audio(src="Hopper.mp3", volume=1, balance=0)
    page.overlay.append(Hopper)
    
    McCarthy = ft.Audio(src="McCarthy.mp3", volume=1, balance=0)
    page.overlay.append(McCarthy)
    
    Berners = ft.Audio(src="Berners.mp3", volume=1, balance=0)
    page.overlay.append(Berners)
    
    Ritchie = ft.Audio(src="Ritchie.mp3", volume=1, balance=0)
    page.overlay.append(Ritchie)
    
    Thompson = ft.Audio(src="Thompson.mp3", volume=1, balance=0)
    page.overlay.append(Thompson)
    
    Gosling = ft.Audio(src="Gosling.mp3", volume=1, balance=0)
    page.overlay.append(Gosling)
    
    Jobs = ft.Audio(src="Jobs.mp3", volume=1, balance=0)
    page.overlay.append(Jobs)
    
    Wozniak= ft.Audio(src="Wozniak.mp3", volume=1, balance=0)
    page.overlay.append(Wozniak)
    
    Gates = ft.Audio(src="Gates.mp3", volume=1, balance=0)
    page.overlay.append(Gates)
    
    Zuckerberg = ft.Audio(src="Zuckerberg.mp3", volume=1, balance=0)
    page.overlay.append(Zuckerberg)
    
    Pages = ft.Audio(src="Pages.mp3", volume=1, balance=0)
    page.overlay.append(Pages)
    
    Brin = ft.Audio(src="Brin.mp3", volume=1, balance=0)
    page.overlay.append(Brin)

    #Audios Evolucion de lenguajes

    Definición = ft.Audio(src="Definición.mp3", volume=1, balance=0)
    page.overlay.append(Definición)

    primer1843 = ft.Audio(src="primer1843.mp3", volume=1, balance=0)
    page.overlay.append(primer1843)
    
    Assembler = ft.Audio(src="Assembler.mp3", volume=1, balance=0)
    page.overlay.append(Assembler)
    
    Fortran = ft.Audio(src="Fortran.mp3", volume=1, balance=0)
    page.overlay.append(Fortran)
    
    List= ft.Audio(src="List.mp3", volume=1, balance=0)
    page.overlay.append(List)
    
    Cobol = ft.Audio(src="Cobol.mp3", volume=1, balance=0) 
    page.overlay.append(Cobol)
    
    Basic = ft.Audio(src="Basic.mp3", volume=1, balance=0)
    page.overlay.append(Basic)
    
    C = ft.Audio(src="C.mp3", volume=1, balance=0)
    page.overlay.append(C)
    
    Pascal1970 = ft.Audio(src="Pascal1970.mp3", volume=1, balance=0)
    page.overlay.append(Pascal1970)
    
    Ada1980 = ft.Audio(src="Ada1980.mp3", volume=1, balance=0)
    page.overlay.append(Ada1980)
    
    Cmasmas = ft.Audio(src="Cmasmas.mp3", volume=1, balance=0)
    page.overlay.append(Cmasmas)
    
    Perl = ft.Audio(src="Perl.mp3", volume=1, balance=0)
    page.overlay.append(Perl)
    
    Python = ft.Audio(src="Python.mp3", volume=1, balance=0)
    page.overlay.append(Python)
    
    VisualBasic = ft.Audio(src="VisualBasic.mp3", volume=1, balance=0)
    page.overlay.append(VisualBasic)
    
    Ruby = ft.Audio(src="Ruby.mp3", volume=1, balance=0)
    page.overlay.append(Ruby)
    
    PHP = ft.Audio(src="PHP.mp3", volume=1, balance=0)
    page.overlay.append(PHP)
    
    Java = ft.Audio(src="Java.mp3", volume=1, balance=0)
    page.overlay.append(Java)
    
    Javascript= ft.Audio(src="Javascript.mp3", volume=1, balance=0)
    page.overlay.append(Javascript)
    
    Csharp = ft.Audio(src="Csharp.mp3", volume=1, balance=0)
    page.overlay.append(Csharp)
    
    Scala = ft.Audio(src="Scala.mp3", volume=1, balance=0)
    page.overlay.append(Scala)
    
    RubyOnRails = ft.Audio(src="RubyOnRails.mp3", volume=1, balance=0)
    page.overlay.append(RubyOnRails)

    def StopAll():
        intro.pause()
        Pascal.pause()
        Leibniz.pause()
        Babbage.pause()
        Lovelace.pause()
        Hollerith.pause()
        Turing.pause()
        Neumann.pause()
        Shannon.pause()
        Hopper.pause()
        McCarthy.pause()
        Berners.pause()
        Ritchie.pause()
        Thompson.pause()
        Gosling.pause()
        Jobs.pause()
        Wozniak.pause()
        Gates.pause()
        Zuckerberg.pause()
        Pages.pause()
        Brin.pause()
        Definición.pause()
        primer1843.pause()
        Assembler.pause()
        Fortran.pause()
        List.pause()
        Cobol.pause()
        Pascal1970.pause()
        Ada1980.pause()
        Cmasmas.pause()
        Perl.pause()
        Python.pause()
        VisualBasic.pause()
        Ruby.pause()
        PHP.pause()
        Java.pause()
        Javascript.pause()
        Csharp.pause()
        Scala.pause()
        RubyOnRails.pause()
        
    
    def play_intro(e):
        StopAll()
        intro.play()
        
    def play_pascal(e):
        StopAll()
        Pascal.play()
        
    def play_leibniz(e):
        StopAll()
        Leibniz.play()
        
    def play_babbage(e):
        StopAll()
        Babbage.play()
        
    def play_lovelace(e):    
        StopAll()
        Lovelace.play()
        
    def play_hollerith(e):
        StopAll()
        Hollerith.play()
        
    def play_turing(e):
        StopAll()
        Turing.play()
    
    def play_neumann(e):
        StopAll()
        Neumann.play()
        
    def play_shannon(e):
        StopAll()
        Shannon.play()
    
    def play_hopper(e):
        StopAll()
        Hopper.play()
    
    def play_mccarthy(e):
        StopAll()
        McCarthy.play()
    
    def play_berners(e):
        StopAll()
        Berners.play()
    
    def play_ritchie(e):
        StopAll()
        Ritchie.play()
        
    def play_thompson(e):
        StopAll()
        Thompson.play()
        
    def play_gosling(e):
        StopAll()
        Gosling.play()
        
    def play_jobs(e):
        StopAll()
        Jobs.play()
        
    def play_wozniak(e):
        StopAll()
        Wozniak.play()
        
    def play_gates(e):
        StopAll()
        Gates.play()
    
    def play_zuckerberg(e):
        StopAll()
        Zuckerberg.play()
    
    def play_pages(e):
        StopAll()
        Pages.play()
    
    def play_brin(e):
        StopAll()
        Brin.play()

    def play_Definicion(e):
        StopAll()
        Definición.play()
        
    def play_primer1843(e):
        StopAll()
        primer1843.play()

    def play_Assembler(e):
        StopAll()
        Assembler.play()

    def play_Fortran(e):
        StopAll()
        Fortran.play()

    def play_List(e):
        StopAll()
        List.play()

    def play_Cobol(e):
        StopAll()
        Cobol.play()

    def play_Pascal1970(e):
        StopAll()
        Pascal1970.play()

    def play_Ada1980(e):
        StopAll()
        Ada1980.play()

    def play_Cmasmas(e):
        StopAll()
        Cmasmas.play()

    def play_Perl(e):
        StopAll()
        Perl.play()

    def play_Python(e):
        StopAll()
        Python.play()

    def play_VisualBasic(e):
        StopAll()
        VisualBasic.play()

    def play_Ruby(e):
        StopAll()
        Ruby.play()

    def play_PHP(e):
        StopAll()
        PHP.play()

    def play_Java(e):
        StopAll()
        Java.play()

    def play_Javascript(e):
        StopAll()
        Javascript.play()

    def play_Csharp(e):
        StopAll()
        Csharp.play()

    def play_Scala(e):
        StopAll()
        Scala.play()

    def play_RubyOnRails(e):
        StopAll()
        RubyOnRails.play()


    # Botones Padres de la informática con imágenes y etiquetas semánticas
    btn1 = ElevatedButton(content=ft.Image(src="Pascal.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Blaise Pascal"), on_click=play_pascal)
    btn2 = ElevatedButton(content=ft.Image(src="Leibniz.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Gottfried Wilhelm Leibniz"), on_click=play_leibniz)
    btn3 = ElevatedButton(content=ft.Image(src="babbage.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Charles Babbage"), on_click=play_babbage)
    btn4 = ElevatedButton(content=ft.Image(src="Lovelace.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ada Lovelace"), on_click=play_lovelace)
    btn5 = ElevatedButton(content=ft.Image(src="Hollerith.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Herman Hollerith"), on_click=play_hollerith)
    btn6 = ElevatedButton(content=ft.Image(src="Turing.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Alan Turing"), on_click=play_turing)
    btn7 = ElevatedButton(content=ft.Image(src="Neumann.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John von Neumann"), on_click=play_neumann)
    btn8 = ElevatedButton(content=ft.Image(src="shannon.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Claude Shannon"), on_click=play_shannon)
    btn9 = ElevatedButton(content=ft.Image(src="Hopper.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Grace Hopper"), on_click=play_hopper)
    btn10 = ElevatedButton(content=ft.Image(src="McCarthy.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John McCarthy"), on_click=play_mccarthy)
    btn11 = ElevatedButton(content=ft.Image(src="Berners.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Tim Berners-Lee"), on_click=play_berners)
    btn12 = ElevatedButton(content=ft.Image(src="Ritchie.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Dennis Ritchie"), on_click=play_ritchie)
    btn13 = ElevatedButton(content=ft.Image(src="Thompson.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ken Thompson"), on_click=play_thompson)
    btn14= ElevatedButton(content=ft.Image(src="Gosling.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="James Gosling"), on_click=play_gosling)
    btn15 = ElevatedButton(content=ft.Image(src="Jobs.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Jobs"), on_click=play_jobs)
    btn16 = ElevatedButton(content=ft.Image(src="Wozniak.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Wozniak"), on_click=play_wozniak)
    btn17 = ElevatedButton(content=ft.Image(src="Gates.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Bill Gates"), on_click=play_gates)
    btn18 = ElevatedButton(content=ft.Image(src="Zuckerberg.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Mark Zuckerberg"), on_click=play_zuckerberg)
    btn19 = ElevatedButton(content=ft.Image(src="Pages.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Larry Page"), on_click=play_pages)
    btn20 = ElevatedButton(content=ft.Image(src="Brin.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Sergey Brin"), on_click=play_brin)

    #Botones de evolucion de lenguajes
    btn21 = ElevatedButton(content=ft.Image(src="Definición.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Definición"), on_click=play_Definicion)
    btn22 = ElevatedButton(content=ft.Image(src="primer1843.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="primer1843"), on_click=play_primer1843)
    btn23 = ElevatedButton(content=ft.Image(src="Assembler.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Assembler"), on_click=play_Assembler)
    btn24 = ElevatedButton(content=ft.Image(src="Fortran.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Fortran"), on_click=play_Fortran)
    btn25 = ElevatedButton(content=ft.Image(src="List.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="List"), on_click=play_List)
    btn26 = ElevatedButton(content=ft.Image(src="Cobol.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Cobol"), on_click=play_Cobol)
    btn27 = ElevatedButton(content=ft.Image(src="Pascal1970.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Pascal1970"), on_click=play_Pascal1970)
    btn28 = ElevatedButton(content=ft.Image(src="Ada1980.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ada1980"), on_click=play_Ada1980)
    btn29 = ElevatedButton(content=ft.Image(src="Cmasmas.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Cmasmas"), on_click=play_Cmasmas)
    btn30 = ElevatedButton(content=ft.Image(src="Perl.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Perl"), on_click=play_Perl)
    btn31 = ElevatedButton(content=ft.Image(src="Python.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Pyhton"), on_click=play_Python)
    btn32 = ElevatedButton(content=ft.Image(src="VisualBasics.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="VisualBasics1991"), on_click=play_VisualBasic)
    btn33 = ElevatedButton(content=ft.Image(src="Ruby.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ruby"), on_click=play_Ruby)
    btn34 = ElevatedButton(content=ft.Image(src="PHP.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="PHP"), on_click=play_PHP)
    btn35 = ElevatedButton(content=ft.Image(src="Java.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Java"), on_click=play_Java)
    btn36 = ElevatedButton(content=ft.Image(src="Javascript.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Javascript"), on_click=play_Javascript)
    btn37 = ElevatedButton(content=ft.Image(src="Csharp.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Csharp"), on_click=play_Csharp)
    btn38 = ElevatedButton(content=ft.Image(src="Scala.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Scala"), on_click=play_Scala)
    btn39 = ElevatedButton(content=ft.Image(src="RubyOnRails.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="RubyOnRails"), on_click=play_RubyOnRails)
    


    
    
    
# Manejo del cambio de ruta
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
        
        # Vista de portada
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("La historia de la Informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Los padres de la informática',
                                        on_click=lambda _: [StopAll(), page.go('/padres')]),
                                    ft.ElevatedButton(
                                        'evolución de los lenguajes de programación',
                                        on_click=lambda _: [StopAll(),page.go('/lenguajes')]),
                                    ft.Image(
                                        src="Portada.png",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Escucha el intro",
                                        on_click=play_intro
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Vista de los padres de la informática
        elif page.route == '/padres':
            page.views.append(
                View(
                    "/padres",
                    controls=[
                        AppBar(
                            title=ft.Text("Los padres de la informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3,btn4
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn5, btn6, btn7,btn8
                                        ]  
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn9, btn10, btn11,btn12
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn13,btn14,btn15,btn16
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn17,btn18,btn19,btn20
                                        ] 
                                    ),
                                    ElevatedButton(
                                        'La evolución de los lenguajes de programación',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # Vista de la evolución de los lenguajes de programación
        elif page.route == '/lenguajes':
            page.views.append(
                View(
                    "/lenguajes",
                    controls=[
                        AppBar(
                            title=ft.Text("La evolución de los lenguajes de programación"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Los padres de la informática',
                                        on_click=lambda _: page.go('/padres')
                                    ),
                                    ft.Text("Los lenguajes de programación han evolucionado a lo largo de la historia, aquí te presentamos algunos de los más importantes:"),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn21, btn22, btn23, btn24
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn25, btn26, btn27, btn28
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn29, btn30, btn31, btn32
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn33, btn34, btn35, btn36
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn37, btn38, btn39
                                        ]
                                    ),
                                    ElevatedButton(
                                        'La evolucion de los lenguajes de programacion',
                                        on_click=lambda _: page.go('/lenguajes')

                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
#ft.app(target=main,view=ft.WEB_BROWSER, assets_dir="assets")
