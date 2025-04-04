from typing import List
import flet as ft
import asyncio

class ProjectImage(ft.View):
    def __init__(self, page: ft.Page, src: List[str], title: str, sub_title: str, theme_mode: ft.ThemeMode):
        super().__init__(bgcolor="#0c0f14")
        self.page = page
        self.img_src = src
        self.title = title
        self.sub_title = sub_title
        self.theme_mode = theme_mode
        self.index = 0
        self.load_img = self.img_src[self.index]
        self.progress = ft.ProgressRing(width=60, height=60, color=ft.Colors.PURPLE)
        self.controls.append(ft.Container(content=self.progress, alignment=ft.alignment.center, expand=True))

        # Kick off async load
        self.page.run_task(self.load_and_display_image)

    # async def load_and_display_image(self):
    #     try:
    #         async with httpx.AsyncClient() as client:
    #             response = await client.get(self.load_img, timeout=2)
    #             if response.status_code != 200:
    #                 # Fallback: show progress while retrying
    #                 for _ in range(5):
    #                     await asyncio.sleep(0.5)
    #                     response = await client.get(self.load_img, timeout=2)
    #                     if response.status_code == 200:
    #                         break
    #     except Exception:
    #         pass

    #     # Minimal wait
    #     await asyncio.sleep(0.2)

    #     self.controls.clear()
    #     self.build_view()
    #     self.page.update()
    
    # I'm skipping httpx check
    async def load_and_display_image(self):
        # await asyncio.sleep(0.3)  # small UX delay
        self.controls.clear()
        self.build_view()
        self.page.update()



    def build_view(self):
        self.main_container = ft.Container(
            alignment=ft.alignment.center,
            margin=10,
            expand=True,
            image=ft.DecorationImage(src=self.load_img, fit=ft.ImageFit.CONTAIN),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Container(on_click=self.close_productpage, width=30, height=30, border_radius=10,
                                         content=ft.Icon(ft.icons.KEYBOARD_ARROW_LEFT, color=ft.Colors.PURPLE)),
                            ft.Container(on_click=self.add_favorites, width=30, height=30, border_radius=10,
                                         content=ft.Icon(ft.icons.FAVORITE, color=ft.Colors.PURPLE)),
                        ]
                    ),
                    ft.Row(
                        expand=1,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.ElevatedButton("PREVIOUS", icon=ft.Icons.KEYBOARD_DOUBLE_ARROW_LEFT_OUTLINED, width=120,
                                              on_click=lambda e: self.change_image(e, -1),
                                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))),
                            ft.ElevatedButton("FORWARD", icon=ft.Icons.KEYBOARD_DOUBLE_ARROW_RIGHT_OUTLINED, width=120,
                                              on_click=lambda e: self.change_image(e, 1),
                                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))
                        ]
                    )
                ]
            )
        )
        self.controls.append(self.main_container)

    def change_image(self, e, direction):
        self.index += direction
        if self.index < 0:
            self.index = len(self.img_src) - 1
        elif self.index >= len(self.img_src):
            self.index = 0

        self.load_img = self.img_src[self.index]
        self.controls.clear()
        self.controls.append(ft.Container(content=self.progress, alignment=ft.alignment.center, expand=True))
        self.page.update()
        self.page.run_task(self.load_and_display_image)

    def close_productpage(self, e):
        self.page.views.pop()
        self.page.update()

    def add_favorites(self, e):
        pass

       

    


class Portfolio(ft.Container) :
    def __init__(self, page : ft.Page):
        super().__init__()
        
        self.page = page
        self.page.padding = 0
        self.page.fonts = {"Starjhol": "../assets/Starjhol.ttf"}
        self.text_fonts = "Tahoma"
        
        self.color_primary = ft.Colors.PURPLE_400
        self.build()
    
    # Work Images
    def work_images(self,e):
        img_src = []
        if e == 0 :
            img_src = ["/resturant/resturant_1.png","/resturant/resturant_2.png","/resturant/resturant_3.png","/resturant/resturant_4.png","/resturant/resturant_5.png","/resturant/resturant_6.png","/resturant/resturant_7.png","/resturant/resturant_8.png"]
        elif e == 1 :
            img_src = ["/mario/mario1.png","/mario/mario2.png","/mario/mario3.png","/mario/mario4.png","/mario/mario5.png","/mario/mario6.png","/mario/mario7.png","/mario/mario8.png","/mario/mario9.png"]
        elif e == 3 :
            self.page.launch_url("https://github.com/frelixnero/my_fastapi_backend")
        elif e == 4 :
            img_src = ["/database/database1.png","/database/database2.png","/database/database3.png","/database/database4.png","/database/database5.png"]
        elif e == 5 :
            self.page.launch_url("https://github.com/frelixnero/Paystack_Verfication_with_FastApi_for_Flutter_apps")
        elif e == 6 :
            img_src = ["/habit/habit_app_1.jpg","/habit/habit_app_2.jpg","/habit/habit_app_3.jpg","/habit/habit_app_4.jpg","/habit/habit_app_5.jpg", "/habit/habit_app_6.jpg", "/habit/habit_app_7.jpg", "/habit/habit_app_8.jpg"]
        
        image_view = ProjectImage(page=self.page, src=img_src, title="testing", sub_title="any", theme_mode=self.page.theme_mode) 
        
        self.page.views.append(image_view)
        self.page.update()
    
        
    def build(self) :
        self.switch_mode = ft.IconButton(icon = ft.icons.DARK_MODE, bgcolor = ft.Colors.DEEP_PURPLE_900, on_click = self.dark_mode)
        
        
        self.animation_style = ft.animation.Animation(1000, ft.AnimationCurve.EASE_OUT_CUBIC)
        
        self.start_frame =ft.Container(
            expand = True,
            # bgcolor = "grey",
            animate_offset = self.animation_style,
            offset = ft.transform.Offset(0,0),
            content =ft.Row(
                spacing = 10,
                expand = True,
                controls = [
                   ft.Container(
                        margin = 20,
                        expand = True,
                        content = ft.Column(
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            controls = [
                               ft.Text("Hello", size = 30, weight = ft.FontWeight.W_800),
                               ft.Text("I'm Osita", size = 30, weight = ft.FontWeight.W_800, color = self.color_primary),
                               ft.Row(
                                    expand = True,
                                    spacing = 0,
                                    controls = [
                                        ft.ElevatedButton( content = ft.Image(
                                            src =   "/linkedin.png",
                                            fit = ft.ImageFit.COVER, width = 20, 
                                        ),
                                            on_click =  lambda e: self.open_url(0),
                                         style = ft.ButtonStyle(side = ft.BorderSide(1, self.color_primary),shape = ft.CircleBorder(),
                                                             overlay_color = {"hovered" : self.color_primary}),           
                                            height = 40,                                        
                                        ),
                                        ft.ElevatedButton( content = ft.Image(
                                            src = "/github.png",
                                            fit = ft.ImageFit.COVER, width = 20, 
                                        ),
                                            on_click =  lambda e: self.open_url(1),
                                         style = ft.ButtonStyle(side = ft.BorderSide(1, self.color_primary),shape = ft.CircleBorder(),
                                                             overlay_color = {"hovered" : self.color_primary}),           
                                            height = 40,                                        
                                        ),
                                        ft.ElevatedButton( content = ft.Image(
                                            src = "/youtube.png",
                                            fit = ft.ImageFit.COVER, width = 20, 
                                        ),
                                         style = ft.ButtonStyle(side = ft.BorderSide(1, self.color_primary),shape = ft.CircleBorder(),
                                                             overlay_color = {"hovered" : self.color_primary}),           
                                            height = 40,                                        
                                        ),
                                    ]
                                )
                            ]
                        )
                    ),
                    ft.Divider(10),
                    
                   ft.Container(
                        expand = True,
                        shape = ft.BoxShape.CIRCLE,
                        clip_behavior = ft.ClipBehavior.ANTI_ALIAS,
                        margin = 50,
                        shadow = ft.BoxShadow(
                            spread_radius = 20,
                            blur_radius = 20,
                            color = self.color_primary
                            ),
                        content = ft.Image(
                            src = "/foto.jpg"
                        )
                    )
                ]
            )
        )
        self.service_frame =ft.Container(
            expand = True,
            animate_offset = self.animation_style,
            offset = ft.transform.Offset(-2,0),
            content = ft.Column(
                scroll = "auto",
                expand = True,
                controls = [
                    ft.ResponsiveRow(
                        expand = True,
                        spacing = 20,
                        controls = [
                           ft.Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 250,
                                      padding = 10,
                                      border = ft.Border(bottom = ft.BorderSide(2, self.color_primary)),
                                      content = ft.Column(
                                          controls = [
                                           ft.Row(
                                              expand = True,
                                              alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                                              vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                              spacing = 20,
                                              controls = [
                                                 ft.Text("01", size = 30, weight = ft.FontWeight.W_900,
                                                       font_family = "Starjhol",),
                                                  ft.ElevatedButton("more", icon=ft.Icons.KEYBOARD_DOUBLE_ARROW_RIGHT_OUTLINED, width=100,
                                                        on_click =  lambda e: self.work_images(0),  # Pass -1 for previous
                                                        style=ft.ButtonStyle(overlay_color={"hovered": self.color_primary}, elevation=20,
                                                                            shape=ft.RoundedRectangleBorder(radius=10),
                                                                            side=ft.BorderSide(1, self.color_primary))),
                                                ]
                                            ),
                                            
                                           ft.Text("Restaurant & Home Delivery App (Flutter, Firebase, FastAPI, Hive)", size = 30, weight = ft.FontWeight.W_900),
                                            
                                           ft.Text(size = 12, value = '''Developed a food ordering app with account registration & Firebase authentication.Implemented a FastAPI backend for processing payments & verifying transactions.Transactions stored both in Firebase Firestore and locally with Hive & SharedPreferences. Users can view & update order statuses, while an admin panel (in progress) manages all orders.Also added a light and darkode which users can change in the settings .''',
                                                 font_family = self.text_fonts)
                                          ]
                                          
                                      )
                                      ),
                           ft.Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 250,
                                      padding = 10,
                                      border = ft.Border(bottom = ft.BorderSide(2, self.color_primary)),
                                      content = ft.Column(
                                          controls = [
                                           ft.Row(
                                              expand = True,
                                              alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                                              vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                              spacing = 20,
                                              controls = [
                                                 ft.Text("02", size = 30, weight = ft.FontWeight.W_900,
                                                       font_family = "Starjhol"),
                                                  ft.ElevatedButton("more", icon=ft.Icons.KEYBOARD_DOUBLE_ARROW_RIGHT_OUTLINED, width=100,
                                                        on_click =  lambda e: self.work_images(1),  # Pass -1 for previous
                                                        style=ft.ButtonStyle(overlay_color={"hovered": self.color_primary}, elevation=20,
                                                                            shape=ft.RoundedRectangleBorder(radius=10),
                                                                            side=ft.BorderSide(1, self.color_primary))),
                                              ]
                                          ),
                                           ft.Text("Mario-style Platformer with Level Editor (Pygame, Python)", size = 30, weight = ft.FontWeight.W_900),
                                            
                                           ft.Text(size = 12, 
                                                 value = 'Built a 2D platformer with a custom level editor allowing users to create & modify levels. Utilized advanced data structures (dictionaries, lists, objects) for game logic.Probably my most complex and demandin gprojects, involving intricate collision detection & game mechanics.',
                                                 font_family = self.text_fonts)
                                          ]
                                          
                                      )
                                      ),
                           ft.Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 200,
                                      padding = 10,
                                      border = ft.Border(bottom = ft.BorderSide(2, self.color_primary)),
                                      content = ft.Column(
                                          controls = [
                                           ft.Row(
                                              expand = True,
                                              alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                                              vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                              spacing = 20,
                                              controls = [
                                                 ft.Text("03", size = 30, weight = ft.FontWeight.W_900,
                                                       font_family = "Starjhol"),
                                                  ft.ElevatedButton("more", icon=ft.Icons.KEYBOARD_DOUBLE_ARROW_RIGHT_OUTLINED, width=100,
                                                        on_click =  lambda e: self.work_images(3),  # Pass -1 for previous
                                                        style=ft.ButtonStyle(overlay_color={"hovered": self.color_primary}, elevation=20,
                                                                            shape=ft.RoundedRectangleBorder(radius=10),
                                                                            side=ft.BorderSide(1, self.color_primary))),
                                              ]
                                          ),


                                           ft.Text("FastAPI Backend for a Social Media App (FastAPI, JWT, PostgreSQL)", size = 30, weight = ft.FontWeight.W_900),
                                            
                                           ft.Text(size = 12, value = "Developed a RESTful backend allowing users to create accounts & authenticate with JWT. Users can create, like, and fetch posts, as well as retrieve all users. Optimized database queries for performance & security.",
                                                 font_family = self.text_fonts)
                                          ]
                                          
                                      )
                                      ),
                           ft.Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 200,
                                      padding = 10,
                                      border = ft.Border(bottom = ft.BorderSide(2, self.color_primary)),
                                      content = ft.Column(
                                          controls = [
                                           ft.Row(
                                              expand = True,
                                              alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                                              vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                              spacing = 20,
                                              controls = [
                                                 ft.Text("04", size = 30, weight = ft.FontWeight.W_900,
                                                       font_family = "Starjhol"),
                                                  ft.ElevatedButton("more", icon=ft.Icons.KEYBOARD_DOUBLE_ARROW_RIGHT_OUTLINED, width=100,
                                                        on_click =  lambda e: self.work_images(4),  # Pass -1 for previous
                                                        style=ft.ButtonStyle(overlay_color={"hovered": self.color_primary}, elevation=20,
                                                                            shape=ft.RoundedRectangleBorder(radius=10),
                                                                            side=ft.BorderSide(1, self.color_primary))),
                                              ]
                                          ),
                                           ft.Text("Personal Database App (Flutter, SQLite)", size = 30, weight = ft.FontWeight.W_900),
                                            
                                           ft.Text(size = 12, value = "Built a CRUD-based database app where users can store personal information (Name, Age, Email, Address). Implemented SQLite database for local storage.",
                                                 font_family = self.text_fonts)
                                          ]
                                          
                                      )
                                      ),
                           ft.Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 200,
                                      padding = 10,
                                      border = ft.Border(bottom = ft.BorderSide(2, self.color_primary)),
                                      content = ft.Column(
                                          controls = [
                                           ft.Row(
                                              expand = True,
                                              alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                                              vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                              spacing = 20,
                                              controls = [
                                                 ft.Text("05", size = 30, weight = ft.FontWeight.W_900,
                                                       font_family = "Starjhol"),
                                                  ft.ElevatedButton("more", icon=ft.Icons.KEYBOARD_DOUBLE_ARROW_RIGHT_OUTLINED, width=100,
                                                        on_click =  lambda e: self.work_images(3),  # Pass -1 for previous
                                                        style=ft.ButtonStyle(overlay_color={"hovered": self.color_primary}, elevation=20,
                                                                            shape=ft.RoundedRectangleBorder(radius=10),
                                                                            side=ft.BorderSide(1, self.color_primary))),
                                              ]
                                          ),
                                           ft.Text("Paystack Payment Processor for Mobile Apps (FastAPI, Paystack API, Flutter)", size = 30, weight = ft.FontWeight.W_900),
                                            
                                           ft.Text(size = 12, value = "Developed a FastAPI backend for initiating & verifying Paystack transactions in Flutter apps. Ensured secure payment processing & seamless integration with mobile applications.",
                                                 font_family = self.text_fonts)
                                          ]
                                          
                                      )
                                      ),
                           ft.Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 200,
                                      padding = 10,
                                      border = ft.Border(bottom = ft.BorderSide(2, self.color_primary)),
                                      content = ft.Column(
                                          controls = [
                                           ft.Row(
                                              expand = True,
                                              alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                                              vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                              spacing = 20,
                                              controls = [
                                                ft.Text("06", size = 30, weight = ft.FontWeight.W_900,
                                                       font_family = "Starjhol"),
                                                ft.ElevatedButton("more", icon=ft.Icons.KEYBOARD_DOUBLE_ARROW_RIGHT_OUTLINED, width=100,
                                                    on_click =  lambda e: self.work_images(6),  # Pass -1 for previous
                                                    style=ft.ButtonStyle(overlay_color={"hovered": self.color_primary}, elevation=20,
                                                                        shape=ft.RoundedRectangleBorder(radius=10),
                                                                        side=ft.BorderSide(1, self.color_primary))),
                                                ]
                                          ),
                                           ft.Text("Habit Tracker App with Calendar Heatmap (Flutter, Isar)", size = 30, weight = ft.FontWeight.W_900),
                                            
                                           ft.Text(size = 12, value = "Designed a habit tracking app where users can log daily activities using a calendar heatmap. Integrated Isar database for data storage and Flutter animations for an engaging UI",
                                                 font_family = self.text_fonts)
                                          ]
                                          
                                      )
                                      ),
                        ]
                    )
                ]
            )
        )
        self.summary_title =ft.Text("My Experience", size = 30, weight = ft.FontWeight.W_900)
        
        # differentft.Containers for each reusme frames
        self.experience_frame =ft.Container(
            expand = True,
            content = ft.Column(
                spacing = 10,
                visible = True,
                alignment = ft.MainAxisAlignment.CENTER,
                expand = True,
                controls = [
                   ft.Container(
                        expand = True,
                        content =ft.Row(
                            expand = True,
                            alignment = ft.MainAxisAlignment.CENTER,
                            controls = [
                               ft.Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = ft.Column(
                                        controls = [
                                           ft.Text("May of 2022 - December of 2022", size = 20, weight = ft.FontWeight.W_900),
                                           ft.Text("The Lord is Good Computer Ltd", size = 15, weight = ft.FontWeight.W_400),
                                            
                                            
                                            
                                        ]
                                    )
                                ),
                               ft.Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = ft.Column(
                                        controls = [
                                           ft.Text("January of 2023 - July of 2023", size = 18, weight = ft.FontWeight.W_900),
                                           ft.Text("Not By Might Company (N.B.M.C.)", size = 12, weight = ft.FontWeight.W_400),
                                            
                                            
                                            
                                        ]
                                    )
                                )
                            ]
                        )
                    ),
                   ft.Container(
                        expand = True,
                        content =ft.Row(
                            expand = True,
                            alignment = ft.MainAxisAlignment.CENTER,
                            controls = [
                               ft.Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = ft.Column(
                                        controls = [
                                           ft.Text(" June of 2024 - November of 2024", size = 18, weight = ft.FontWeight.W_900),
                                           ft.Text("DesDev IT Solutions", size = 12, weight = ft.FontWeight.W_400),
                                            
                                            
                                            
                                        ]
                                    )
                                ),
                               ft.Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = ft.Column(
                                        controls = [
                                           ft.Text("2024 - Present", size = 18, weight = ft.FontWeight.W_900),
                                           ft.Text("", size = 12, weight = ft.FontWeight.W_400),
                                           ft.Text("", size = 12, font_family = self.text_fonts),
                                            
                                            
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.education_frame =ft.Container(
            expand = True,
            visible = False,
            content = ft.Column(
                spacing = 10,
                visible = True,
                alignment = ft.MainAxisAlignment.CENTER,
                expand = True,
                controls = [
                   ft.Container(
                        expand = True,
                        content =ft.Row(
                            expand = True,
                            alignment = ft.MainAxisAlignment.CENTER,
                            controls = [
                               ft.Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = ft.Column(
                                        controls = [
                                           ft.Text("2001 - 2012", size = 20, weight = ft.FontWeight.W_900),
                                           ft.Text("Elementary Education", size = 15, weight = ft.FontWeight.W_400),
                                           ft.Text("Pinecrest Group of Schools, Enugu", size = 12, font_family = self.text_fonts),
                                            
                                            
                                        ]
                                    )
                                ),
                               ft.Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = ft.Column(
                                        controls = [
                                           ft.Text("2012 - 2018", size = 20, weight = ft.FontWeight.W_900),
                                           ft.Text("Secondary School Education", size = 15, weight = ft.FontWeight.W_400),
                                           ft.Text("Nigerian Navy Secondary School, Calabar", size = 12, font_family = self.text_fonts),
                                            
                                            
                                        ]
                                    )
                                )
                            ]
                        )
                    ),
                   ft.Container(
                        expand = True,
                        content =ft.Row(
                            expand = True,
                            alignment = ft.MainAxisAlignment.CENTER,
                            controls = [
                               ft.Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = ft.Column(
                                        controls = [
                                           ft.Text("2018 - 2023 ", size = 18, weight = ft.FontWeight.W_900),
                                           ft.Text("University Education", size = 12, weight = ft.FontWeight.W_400),
                                           ft.Text("Nnamdi Azikiwe University, Awka", size = 12, font_family = self.text_fonts),
                                           ft.Text("Majored in Electronics and Computer Engineering", size = 12, font_family = self.text_fonts),
                                            
                                            
                                        ]
                                    )
                                ),
                               ft.Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = ft.Column(
                                        controls = [
                                           ft.Text("2024 - Present", size = 18, weight = ft.FontWeight.W_900),
                                           ft.Text("", size = 12, weight = ft.FontWeight.W_400),
                                           ft.Text("", size = 12, font_family = self.text_fonts),
                                            
                                            
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.skills_frame =ft.Container(
            expand = True,
            visible = False,
            content = ft.Column(
                alignment = ft.MainAxisAlignment.CENTER,
                spacing = 10,
                expand = True,
                controls = [
                   ft.Container(
                        expand = True,
                        content =ft.Row(
                            expand = True,
                            controls = [
                               ft.Container(
                                    expand = True, 
                                    tooltip = "Pygame",
                                    border_radius = 10,
                                    padding = 15,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    content = ft.Image(src = "/pygame_logo2.svg", )
                                ),
                               ft.Container(
                                    expand = True, 
                                    tooltip = "Blender",
                                    border_radius = 10,
                                    padding = 15,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    content = ft.Image(src = "/blender_2.svg", )
                                ),
                               ft.Container(
                                    expand = True,
                                    tooltip = "Python", 
                                    border_radius = 10,
                                    padding = 15,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    content = ft.Image(src = "/python.svg", )
                                ),
                            ]
                        )
                    ),
                   ft.Container(
                        expand = True,
                        content =ft.Row(
                            expand = True,
                            controls = [
                               ft.Container(
                                    expand = True,
                                    tooltip = "Fastapi", 
                                    border_radius = 10,
                                    padding = 15,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    content = ft.Image(src = "/fastapi_svg.svg", height = 150, width = 100 )
                                ),
                               ft.Container(
                                    expand = True, 
                                    tooltip = "Flutter",
                                    border_radius = 10,
                                    padding = 15,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    content = ft.Image(src = "/flutter_svg.svg", expand = True,  height = 150, width = 100  )
                                ),
                               ft.Container(
                                    expand = True,
                                    tooltip = "Flet", 
                                    border_radius = 10,
                                    padding = 15,
                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primary),
                                    content = ft.Image(src = "/flet_svg.svg", )
                                ),
                            ]
                        )
                    )
                ]
            )
        )
        self.resume_frame =ft.Container(
            expand = True,
            animate_offset = self.animation_style,
            offset = ft.transform.Offset(-2,0),
            content = ft.Column(
                expand = True,
                scroll = "auto",
                controls = [
                    ft.ResponsiveRow(
                        spacing = 100,
                        expand = True,
                        controls = [
                           ft.Container(
                                expand = True,
                                margin = 20,
                                height = 400,
                                alignment = ft.alignment.center,
                                col = {"xs":12, "sm":6},
                                content = ft.Column(
                                    expand = True,
                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                    alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                                    controls = [
                                       ft.Text("Why hire me ?",
                                             size = 30,
                                             weight = ft.FontWeight.W_900,
                                             color = self.color_primary,
                                             ),
                                       ft.Text("As a passionate and versatile developer, I bring a unique blend of creativity and technical expertise to the table. With hands-on experience in Python frameworks like Flet, FastAPI, and Pygame coupled with a grounded understanding of modern GUI development with Flutter, I excel at building interactive, user-focused applications that solve real-world problems.", 
                                             
                                             size = 16,
                                             font_family = self.text_fonts,
                                             
                                             ),
                                       ft.TextButton("Experience",
                                                width = 200,
                                                on_click = lambda e: self.change_resume(0),
                                                style = ft.ButtonStyle(
                                                    overlay_color = {"hovered" : self.color_primary},
                                                    shape = ft.RoundedRectangleBorder(radius = 20),
                                                    side = ft.BorderSide(1, self.color_primary),
                                                    
                                                )
                                                
                                                ),
                                       ft.TextButton("Education",
                                                width = 200,
                                                on_click = lambda e: self.change_resume(1),
                                                style = ft.ButtonStyle(
                                                    overlay_color = {"hovered" : self.color_primary},
                                                    shape = ft.RoundedRectangleBorder(radius = 20),
                                                    side = ft.BorderSide(1, self.color_primary),
                                                    
                                                )
                                                
                                                ),
                                       ft.TextButton("Skillset",
                                                width = 200,
                                                on_click = lambda e: self.change_resume(2),
                                                style = ft.ButtonStyle(
                                                    overlay_color = {"hovered" : self.color_primary},
                                                    shape = ft.RoundedRectangleBorder(radius = 20),
                                                    side = ft.BorderSide(1, self.color_primary),
                                                    
                                                )
                                                
                                                )
                                    ]
                                )
                            ),
                           ft.Container(
                                expand = True,
                                margin = 20,
                                height = 400,
                                col = {"xs":12, "sm":6},
                                content = ft.Column(
                                    expand = True,
                                    alignment = ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                    controls = [
                                        self.summary_title,
                                        ft.Stack(
                                            expand = True,
                                            controls = [
                                                self.experience_frame ,
                                                self.education_frame ,
                                                self.skills_frame ,
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.contact_frame =ft.Container(
            expand = True,
            animate_offset = self.animation_style,
            offset = ft.transform.Offset(-2,0),
            content = ft.Column(
                scroll = "auto",
                expand = True,
                controls = [
                    ft.ResponsiveRow(
                        expand = True,
                        controls = [
                           ft.Container(
                                expand = True,
                                margin = 20,
                                height = 400,
                                padding = 10,
                                alignment = ft.alignment.center,
                                col = {
                                    "xs":12, "sm":6
                                },
                                content = ft.Column(
                                    expand = True,
                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                    alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                                    controls = [
                                       ft.Text("Let's work together", size = 30, weight = ft.FontWeight.W_900),
                                       ft.TextField(hint_text = "Email", border_radius = 10, border_color = self.color_primary, ),
                                       ft.TextField(hint_text = "Email", border_radius = 10, border_color = self.color_primary, ),
                                       ft.TextField(hint_text = "Message", border_radius = 10, border_color = self.color_primary, multiline = True, min_lines = 5, max_lines = 6 ),
                                        ft.ElevatedButton(
                                            "Send",
                                            width = 100,
                                            style = ft.ButtonStyle(
                                                overlay_color = {"hovered" : self.color_primary},
                                                elevation = 20,
                                                shape = ft.RoundedRectangleBorder(radius = 20),
                                                side = ft.BorderSide(1, self.color_primary)
                                            )
                                        )
                                        
                                    ]
                                    
                                )
                            ),
                           ft.Container(
                                expand = True,
                                margin = 20,
                                height = 400,
                                padding = 10,
                                alignment = ft.alignment.center,
                                col = {
                                    "xs":12, "sm":6
                                },
                                content = ft.Column(
                                    alignment = ft.MainAxisAlignment.CENTER,
                                    expand = True,
                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                    controls = [
                                       ft.Row(
                                            controls = [
                                                ft.Icon(ft.Icons.PHONE_ANDROID_OUTLINED,),
                                                ft.Column(
                                                    spacing = 0,
                                                    controls = [
                                                       ft.Text("Phone", size = 13, color = self.color_primary),
                                                       ft.Text("+234-81-360-46142", size = 13, weight = ft.FontWeight.W_900, color = self.color_primary),
                                                        
                                                    ]
                                                )
                                            ]
                                        ),
                                       ft.Row(
                                            controls = [
                                                ft.Icon(ft.Icons.EMAIL_OUTLINED,),
                                                ft.Column(
                                                    spacing = 0,
                                                    controls = [
                                                       ft.Text("Email", size = 13, color = self.color_primary),
                                                       ft.Text("osiraogene@gmail.com", size = 13, weight = ft.FontWeight.W_900, color = self.color_primary),
                                                        
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            controls = [
                                                ft.Icon(ft.Icons.LOCATION_ON_OUTLINED,),
                                                ft.Column(
                                                    spacing = 0,
                                                    controls = [
                                                        ft.Text("Location", size = 13, color = self.color_primary),
                                                        ft.Text("Enugu, Nigeria", size = 13, weight = ft.FontWeight.W_900, color = self.color_primary),
                                                        
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment = ft.MainAxisAlignment.START,
                                            spacing = 20,
                                            controls = [
                                                ft.ElevatedButton(
                                                    bgcolor = ft.Colors.with_opacity(0.3, self.color_primary),
                                                    width = 80,
                                                    height = 80,
                                                    on_click =  lambda e: self.open_url(2),
                                                    content =ft.Container(
                                                        padding = 10,
                                                        expand = True,
                                                        content = ft.Image(src = "twitter.svg", width = 80, height = 80),
                                                    )
                                                ),
                                                ft.ElevatedButton(
                                                    bgcolor = ft.Colors.with_opacity(0.3, self.color_primary),
                                                    width = 80,
                                                    height = 80,
                                                    on_click =  lambda e: self.open_url(3),
                                                    content =ft.Container(
                                                        padding = 10,
                                                        expand = True,
                                                        content = ft.Image(src = "instagram_svg.svg", width = 80, height = 80),
                                                    )
                                                ),
                                                ft.ElevatedButton(
                                                    bgcolor = ft.Colors.with_opacity(0.3, self.color_primary),
                                                    width = 80,
                                                    height = 80,
                                                    on_click =  lambda e: self.open_url(4),
                                                    content =ft.Container(
                                                        padding = 10,
                                                        expand = True,
                                                        content = ft.Image(src = "whatsapp.svg", width = 80, height = 80),
                                                    )
                                                ),
                                            ]
                                        ),
                                    ]
                                )
                                
                            )
                        ]
                        
                    )
                ]
            )
        )
        self.content = ft.Column(
            expand = True,
            spacing = 2,
            controls = [
               ft.Container(   #header
                    padding = 20,
                    content = ft.Row(
                        expand = True,
                        controls = [
                           ft.Container(
                                expand = True,
                                margin = ft.margin.only(left = 20, ),
                                content = ft.Text(
                                    size = 20,
                                    spans = [
                                        ft.TextSpan("Frelix", style = ft.TextStyle(color = ft.Colors.PURPLE_100, weight = ft.FontWeight.W_900)),
                                        ft.TextSpan("Nero", style = ft.TextStyle(color = ft.Colors.PURPLE_400, weight = ft.FontWeight.W_900)),
                                        ft.TextSpan(".", style = ft.TextStyle(color = ft.Colors.PURPLE_900, weight = ft.FontWeight.W_900))
                                    ]
                                )
                            ),
                            ft.ResponsiveRow(
                                alignment = ft.MainAxisAlignment.CENTER,
                                spacing = 0,
                                expand = True,
                                controls = [
                                    ft.TextButton("Start", style = ft.ButtonStyle(color = self.color_primary), col ={
                                        "xs":12, "sm":6, "md":3
                                    }, on_click = lambda e: self.change_page(0) ),
                                    ft.TextButton("Services", style = ft.ButtonStyle(color = self.color_primary), col ={
                                        "xs":12, "sm":6, "md":3
                                    }, on_click = lambda e: self.change_page(1) ),
                                    ft.TextButton("Resume", style = ft.ButtonStyle(color = self.color_primary), col ={
                                        "xs":12, "sm":6, "md":3
                                    }, on_click = lambda e: self.change_page(2) ),
                                    ft.TextButton("Contact me", style = ft.ButtonStyle(color = self.color_primary), col ={
                                        "xs":12, "sm":6, "md":3
                                    }, on_click = lambda e: self.change_page(3) )
                                ]
                            ),
                           ft.Container(
                                width = 50,
                                margin = ft.margin.only(right = 20),
                                content = self.switch_mode
                                
                            )
                        
                        
                        ]
                        
                    )
                ),
               ft.Container(          #body
                    expand = True,
                    content = ft.Stack(
                        controls = [
                            self.start_frame,
                            self.service_frame,
                            self.resume_frame,
                            self.contact_frame
                        ]
                    )
                ),
               ft.Container(          #footer
                    padding = 20,
                    gradient = ft.LinearGradient([self.color_primary, ft.Colors.TRANSPARENT], rotation = 0),
                    content = ft.Text("Powered by Flet(Flutter) - All rights reserved",),
                    alignment = ft.alignment.center
                )
            ]
        )
        
        self.page.add(self.content,)
        
    def change_page(self,e) :
        self.start_frame.offset.x = -2
        self.service_frame.offset.x = -2
        self.resume_frame.offset.x = -2
        self.contact_frame.offset.x = -2
        
        if e == 0 :
            self.start_frame.offset.x = 0
        if e == 1 :
            self.service_frame.offset.x = 0
        if e == 2 :
            self.resume_frame.offset.x = 0
        if e == 3 :
            self.contact_frame.offset.x = 0
        
        self.page.update()

    
    def dark_mode(self,e) :
        if e.control.icon == "dark_mode" :
            self.switch_mode.icon = ft.Icons.LIGHT_MODE
            self.page.theme_mode = "light"
        else : 
            self.switch_mode.icon = ft.Icons.DARK_MODE
            self.page.theme_mode = "dark"
        self.page.update()
        
    def change_resume(self,e) :
        self.experience_frame.visible = False
        self.education_frame.visible = False
        self.skills_frame.visible = False
        
        if e == 0 :
            self.experience_frame.visible = True
            self.summary_title.value = "My Experience"
        elif e == 1 : 
            self.education_frame.visible = True
            self.summary_title.value = "My Educational Level"
        elif e == 2 :
            self.skills_frame.visible = True
            self.summary_title.value = "My Skillset"
            
        self.page.update()
        
    def open_url(self,e):
        if e == 0 :
            self.page.launch_url("https://www.linkedin.com/in/osita-felix-368a9b175?trk=contact-info")
        elif e == 1:
            self.page.launch_url("https://github.com/frelixnero")
        elif e == 2 :
            self.page.launch_url("https://x.com/Frelixnero?t=B63-W-Tmvwx3PGMbM9HPWg&s=08")
        elif e == 3 :
            self.page.launch_url("https://www.instagram.com/frelixnero?igsh=YzljYTk1ODg3Zg==")
        elif e == 4 :
            self.page.launch_url("https://wa.me/qr/A3MPE6MABE73F1")
        elif e == 5 :
            self.page.launch_url("https://github.com/frelixnero/my_fastapi_backend")
        elif e == 6 :
            self.page.launch_url("https://github.com/frelixnero/Paystack_Verfication_with_FastApi_for_Flutter_apps")

ft.app(target = lambda page : Portfolio(page), view = ft.WEB_BROWSER, assets_dir = "assets")
