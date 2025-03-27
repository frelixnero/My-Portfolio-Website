# from typing import List
# from flet import *
# import urllib

# class ProjectImage(View):
#     def __init__(self, page: Page,):
#         super(ProjectImage,self).__init__(
#             route = "/project_image",
#             padding = 20,
#             horizontal_alignment = 'center',
#             vertical_alignment = 'center',
            
#         )
#         self.page = page
#         self.img_src = self.page.session.get('images')
#         self.color_food = "#b9894b"
#         self.container_color = "#141821"
#         self.index = 0
#         self.color_primary = Colors.PURPLE_400
#         self.main_container = Container( 
#             alignment=alignment.center,
#             margin=10,
#             expand=True,
#             image=DecorationImage(src=self.img_src[self.index], fit=ImageFit.CONTAIN),
#             content=Column(
#                 alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER, expand=True,
#                 controls=[
#                     Row(
#                         alignment=MainAxisAlignment.SPACE_BETWEEN, controls=[
#                             Container(on_click=self.close_productpage, width=30, height=30, border_radius=10,
#                                       content=Icon(icons.KEYBOARD_ARROW_LEFT, color=self.color_primary)),
#                             Container(on_click=self.add_favorites, width=30, height=30, border_radius=10,
#                                       content=Icon(icons.FAVORITE, color=self.color_primary)),
#                         ]
#                     ),
#                     Row(
#                         expand=1, alignment=MainAxisAlignment.SPACE_BETWEEN,
#                         controls=[
#                             ElevatedButton("PREVIOUS", icon=Icons.KEYBOARD_DOUBLE_ARROW_LEFT_OUTLINED, width=120,
#                                            on_click=lambda e: self.change_image(e, -1),  # Pass -1 for previous
#                                            style=ButtonStyle(overlay_color={"hovered": self.color_primary}, elevation=20,
#                                                              shape=RoundedRectangleBorder(radius=10),
#                                                              side=BorderSide(1, self.color_primary))),
#                             ElevatedButton("FORWARD", icon=Icons.KEYBOARD_DOUBLE_ARROW_RIGHT_OUTLINED, width=120,
#                                            on_click=lambda e: self.change_image(e, 1), # Pass 1 for next
#                                            style=ButtonStyle(overlay_color={"hovered": self.color_primary}, elevation=20,
#                                                              shape=RoundedRectangleBorder(radius=10),
#                                                              side=BorderSide(1, self.color_primary)))
#                         ]
#                     ),
#                 ]
#             ),
#         )
        
#         # for controls
#         self.controls = [
#             self.main_container
#         ]

#     def build_view(self):
#         self.main_container = Container( 
#             alignment=alignment.center,
#             margin=10,
#             expand=True,
#             image=DecorationImage(src=self.img_src[self.index], fit=ImageFit.CONTAIN),
#             content=Column(
#                 alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER, expand=True,
#                 controls=[
#                     Row(
#                         alignment=MainAxisAlignment.SPACE_BETWEEN, controls=[
#                             Container(on_click=self.close_productpage, width=30, height=30, border_radius=10,
#                                       content=Icon(icons.KEYBOARD_ARROW_LEFT, color=self.color_primary)),
#                             Container(on_click=self.add_favorites, width=30, height=30, border_radius=10,
#                                       content=Icon(icons.FAVORITE, color=self.color_primary)),
#                         ]
#                     ),
#                     Row(
#                         expand=1, alignment=MainAxisAlignment.SPACE_BETWEEN,
#                         controls=[
#                             ElevatedButton("PREVIOUS", icon=Icons.KEYBOARD_DOUBLE_ARROW_LEFT_OUTLINED, width=120,
#                                            on_click=lambda e: self.change_image(e, -1),  # Pass -1 for previous
#                                            style=ButtonStyle(overlay_color={"hovered": self.color_primary}, elevation=20,
#                                                              shape=RoundedRectangleBorder(radius=10),
#                                                              side=BorderSide(1, self.color_primary))),
#                             ElevatedButton("FORWARD", icon=Icons.KEYBOARD_DOUBLE_ARROW_RIGHT_OUTLINED, width=120,
#                                            on_click=lambda e: self.change_image(e, 1), # Pass 1 for next
#                                            style=ButtonStyle(overlay_color={"hovered": self.color_primary}, elevation=20,
#                                                              shape=RoundedRectangleBorder(radius=10),
#                                                              side=BorderSide(1, self.color_primary)))
#                         ]
#                     ),
#                 ]
#             ),
#         )
#         self.controls.append(self.main_container)

#     def change_image(self, e, direction): # Added direction parameter
#         self.index += direction

#         if self.index < 0:
#             self.index = len(self.img_src) - 1
#         elif self.index >= len(self.img_src):
#             self.index = 0

#         self.main_container.image.src = self.img_src[self.index]
#         self.page.update()

#     def close_productpage(self, e):
#         self.page.go("/portfolio")
#         self.page.update()

#     def add_favorites(self, e):
#         print("Add to favorites clicked")
#         pass


# class Portfolio(View) :
#     def __init__(self, page : Page) -> None:
#         super(Portfolio,self).__init__(
#             route = "/portfolio",
#             padding = 20,
#             horizontal_alignment = 'center',
#             vertical_alignment = 'center',
            
#         )
        
#         self.page = page
#         self.page.padding = 0
#         self.page.fonts = {"Starjhol": "../assets/Starjhol.ttf"}
#         self.text_fonts = "Tahoma"
#         self.animation_style = animation.Animation(1000, AnimationCurve.EASE_OUT_CUBIC)
#         # ✅ Initialize all components properly
#         self.switch_mode = Switch(value= True if self.page.theme_mode == "light" else False, on_change=self.dark_mode)
#         # self.start_frame = Container(content=Text("Start Page"))
#         # self.service_frame = Container(content=Text("Services Page"))
#         self.resume_frame = Container(content=Text("Resume Page"))
#         # self.contact_frame = Container(content=Text("Contact Page"))

#         self.color_primary = Colors.PURPLE_400
#         self.start_frame = Container(
#             expand = True,
#             # bgcolor = "grey",
#             animate_offset = self.animation_style,
#             offset = transform.Offset(0,0),
#             content = Row(
#                 spacing = 10,
#                 expand = True,
#                 controls = [
#                     Container(
#                         margin = 20,
#                         expand = True,
#                         content = Column(
#                             alignment = MainAxisAlignment.CENTER,
#                             horizontal_alignment = CrossAxisAlignment.CENTER,
#                             controls = [
#                                 Text("Hello", size = 30, weight = FontWeight.W_800),
#                                 Text("I'm Osita", size = 30, weight = FontWeight.W_800, color = self.color_primary),
#                                 Row(
#                                     expand = True,
#                                     spacing = 0,
#                                     controls = [
#                                         ElevatedButton( content = Image(
#                                             src =   "/linkedin.png",
#                                             fit = ImageFit.COVER, width = 20, 
#                                         ),
#                                             on_click =  lambda e: self.open_url(0),
#                                          style = ButtonStyle(side = BorderSide(1, self.color_primary),shape = CircleBorder(),
#                                                              overlay_color = {"hovered" : self.color_primary}),           
#                                             height = 40,                                        
#                                         ),
#                                         ElevatedButton( content = Image(
#                                             src = "/github.png",
#                                             fit = ImageFit.COVER, width = 20, 
#                                         ),
#                                             on_click =  lambda e: self.open_url(1),
#                                          style = ButtonStyle(side = BorderSide(1, self.color_primary),shape = CircleBorder(),
#                                                              overlay_color = {"hovered" : self.color_primary}),           
#                                             height = 40,                                        
#                                         ),
#                                         ElevatedButton( content = Image(
#                                             src = "/youtube.png",
#                                             fit = ImageFit.COVER, width = 20, 
#                                         ),
#                                          style = ButtonStyle(side = BorderSide(1, self.color_primary),shape = CircleBorder(),
#                                                              overlay_color = {"hovered" : self.color_primary}),           
#                                             height = 40,                                        
#                                         ),
#                                     ]
#                                 )
#                             ]
#                         )
#                     ),
#                     Divider(10),
                    
#                     Container(
#                         expand = True,
#                         shape = BoxShape.CIRCLE,
#                         clip_behavior = ClipBehavior.ANTI_ALIAS,
#                         margin = 50,
#                         shadow = BoxShadow(
#                             spread_radius = 20,
#                             blur_radius = 20,
#                             color = self.color_primary
#                             ),
#                         content = Image(
#                             src = "/foto.jpg"
#                         )
#                     )
#                 ]
#             )
#         )
        
        
#         #######  S E R V I C E   F R A M E 
#         self.service_frame = Container(
#             expand = True,
#             animate_offset = self.animation_style,
#             offset = transform.Offset(-2,0),
#             content = Column(
#                 scroll = "auto",
#                 expand = True,
#                 controls = [
#                     ResponsiveRow(
#                         expand = True,
#                         spacing = 20,
#                         controls = [
#                             Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 250,
#                                       padding = 10,
#                                       border = Border(bottom = BorderSide(2, self.color_primary)),
#                                       content = Column(
#                                           controls = [
#                                             Row(
#                                               expand = True,
#                                               alignment = MainAxisAlignment.SPACE_BETWEEN,
#                                               vertical_alignment = CrossAxisAlignment.CENTER,
#                                               spacing = 20,
#                                               controls = [
#                                                   Text("01", size = 30, weight = FontWeight.W_900,
#                                                        font_family = "Starjhol"),
#                                                   IconButton(icon = Icons.ARROW_OUTWARD,
#                                                              style = ButtonStyle(
#                                                                  bgcolor = self.color_primary,
                                                                 
#                                                              ),
#                                                              data = ["/resturant/resturant_1.png","/resturant/resturant_2.png","/resturant/resturant_3.png","/resturant/resturant_4.png","/resturant/resturant_5.png","/resturant/resturant_6.png","/resturant/resturant_7.png","/resturant/resturant_8.png"],
#                                                              on_click=self.go_to_details
                                                             
#                                                              )
#                                               ]
#                                           ),


#                                             Text("Restaurant & Home Delivery App (Flutter, Firebase, FastAPI, Hive)", size = 30, weight = FontWeight.W_900),
                                            
#                                             Text(size = 12, value = '''Developed a food ordering app with account registration & Firebase authentication.Implemented a FastAPI backend for processing payments & verifying transactions.Transactions stored both in Firebase Firestore and locally with Hive & SharedPreferences. Users can view & update order statuses, while an admin panel (in progress) manages all orders.Also added a light and darkode which users can change in the settings .''',
#                                                  font_family = self.text_fonts)
#                                           ]
                                          
#                                       )
#                                       ),
#                             Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 250,
#                                       padding = 10,
#                                       border = Border(bottom = BorderSide(2, self.color_primary)),
#                                       content = Column(
#                                           controls = [
#                                             Row(
#                                               expand = True,
#                                               alignment = MainAxisAlignment.SPACE_BETWEEN,
#                                               vertical_alignment = CrossAxisAlignment.CENTER,
#                                               spacing = 20,
#                                               controls = [
#                                                   Text("02", size = 30, weight = FontWeight.W_900,
#                                                        font_family = "Starjhol"),
#                                                   IconButton(icon = Icons.ARROW_OUTWARD,
#                                                              style = ButtonStyle(
#                                                                  bgcolor = self.color_primary,
                                                                 
#                                                              ),
#                                                              data = ["/mario/mario1.png","/mario/mario2.png","/mario/mario3.png","/mario/mario4.png","/mario/mario5.png","/mario/mario6.png","/mario/mario7.png","/mario/mario8.png","/mario/mario9.png"],
#                                                              on_click= self.go_to_details
#                                                              )
#                                               ]
#                                           ),
#                                             Text("Mario-style Platformer with Level Editor (Pygame, Python)", size = 30, weight = FontWeight.W_900),
                                            
#                                             Text(size = 12, 
#                                                  value = 'Built a 2D platformer with a custom level editor allowing users to create & modify levels. Utilized advanced data structures (dictionaries, lists, objects) for game logic.Probably my most complex and demandin gprojects, involving intricate collision detection & game mechanics.',
#                                                  font_family = self.text_fonts)
#                                           ]
                                          
#                                       )
#                                       ),
#                             Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 200,
#                                       padding = 10,
#                                       border = Border(bottom = BorderSide(2, self.color_primary)),
#                                       content = Column(
#                                           controls = [
#                                             Row(
#                                               expand = True,
#                                               alignment = MainAxisAlignment.SPACE_BETWEEN,
#                                               vertical_alignment = CrossAxisAlignment.CENTER,
#                                               spacing = 20,
#                                               controls = [
#                                                   Text("03", size = 30, weight = FontWeight.W_900,
#                                                        font_family = "Starjhol"),
#                                                   IconButton(icon = Icons.ARROW_OUTWARD,
#                                                              style = ButtonStyle(
#                                                                  bgcolor = self.color_primary,
                                                                 
#                                                              ),
#                                                              on_click= lambda e: self.open_url(5),
#                                                              )
#                                               ]
#                                           ),


#                                             Text("FastAPI Backend for a Social Media App (FastAPI, JWT, PostgreSQL)", size = 30, weight = FontWeight.W_900),
                                            
#                                             Text(size = 12, value = "Developed a RESTful backend allowing users to create accounts & authenticate with JWT. Users can create, like, and fetch posts, as well as retrieve all users. Optimized database queries for performance & security.",
#                                                  font_family = self.text_fonts)
#                                           ]
                                          
#                                       )
#                                       ),
#                             Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 200,
#                                       padding = 10,
#                                       border = Border(bottom = BorderSide(2, self.color_primary)),
#                                       content = Column(
#                                           controls = [
#                                             Row(
#                                               expand = True,
#                                               alignment = MainAxisAlignment.SPACE_BETWEEN,
#                                               vertical_alignment = CrossAxisAlignment.CENTER,
#                                               spacing = 20,
#                                               controls = [
#                                                   Text("04", size = 30, weight = FontWeight.W_900,
#                                                        font_family = "Starjhol"),
#                                                   IconButton(icon = Icons.ARROW_OUTWARD,
#                                                              style = ButtonStyle(
#                                                                  bgcolor = self.color_primary,
                                                                 
#                                                              ),
#                                                              on_click= lambda e:self.go_to_details(2)
#                                                              )
#                                               ]
#                                           ),
#                                             Text("Personal Database App (Flutter, SQLite)", size = 30, weight = FontWeight.W_900),
                                            
#                                             Text(size = 12, value = "Built a CRUD-based database app where users can store personal information (Name, Age, Email, Address). Implemented SQLite database for local storage.",
#                                                  font_family = self.text_fonts)
#                                           ]
                                          
#                                       )
#                                       ),
#                             Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 200,
#                                       padding = 10,
#                                       border = Border(bottom = BorderSide(2, self.color_primary)),
#                                       content = Column(
#                                           controls = [
#                                             Row(
#                                               expand = True,
#                                               alignment = MainAxisAlignment.SPACE_BETWEEN,
#                                               vertical_alignment = CrossAxisAlignment.CENTER,
#                                               spacing = 20,
#                                               controls = [
#                                                   Text("05", size = 30, weight = FontWeight.W_900,
#                                                        font_family = "Starjhol"),
#                                                   IconButton(icon = Icons.ARROW_OUTWARD,
                                                             
#                                                              style = ButtonStyle(
                                                                
#                                                                  bgcolor = self.color_primary,
                                                                 
#                                                              ),
#                                                              on_click= lambda e: self.open_url(6),
#                                                              )
#                                               ]
#                                           ),
#                                             Text("Paystack Payment Processor for Mobile Apps (FastAPI, Paystack API, Flutter)", size = 30, weight = FontWeight.W_900),
                                            
#                                             Text(size = 12, value = "Developed a FastAPI backend for initiating & verifying Paystack transactions in Flutter apps. Ensured secure payment processing & seamless integration with mobile applications.",
#                                                  font_family = self.text_fonts)
#                                           ]
                                          
#                                       )
#                                       ),
#                             Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 200,
#                                       padding = 10,
#                                       border = Border(bottom = BorderSide(2, self.color_primary)),
#                                       content = Column(
#                                           controls = [
#                                             Row(
#                                               expand = True,
#                                               alignment = MainAxisAlignment.SPACE_BETWEEN,
#                                               vertical_alignment = CrossAxisAlignment.CENTER,
#                                               spacing = 20,
#                                               controls = [
#                                                   Text("06", size = 30, weight = FontWeight.W_900,
#                                                        font_family = "Starjhol"),
#                                                   IconButton(icon = Icons.ARROW_OUTWARD,
#                                                              style = ButtonStyle(
#                                                                  bgcolor = self.color_primary,
                                                                 
#                                                              ),
#                                                              on_click= lambda e:self.go_to_details(5)
#                                                              )
#                                                 ]
#                                           ),
#                                             Text("Habit Tracker App with Calendar Heatmap (Flutter, Isar)", size = 30, weight = FontWeight.W_900),
                                            
#                                             Text(size = 12, value = "Designed a habit tracking app where users can log daily activities using a calendar heatmap. Integrated Isar database for data storage and Flutter animations for an engaging UI",
#                                                  font_family = self.text_fonts)
#                                           ]
                                          
#                                       )
#                                       ),
#                         ]
#                     )
#                 ]
#             )
#         )
        
#         # #### C O N T A C T   F R A M E
#         self.contact_frame = Container(
#             expand = True,
#             animate_offset = self.animation_style,
#             offset = transform.Offset(-2,0),
#             content = Text("Contact Page", text_align = alignment.center, size = 100)
#                 # Column(
#                 #     scroll = "auto",
#                 #     expand = True,
#                 #     controls = [
#                 #         ResponsiveRow(
#                 #             expand = True,
#                 #             controls = [
#                 #                 Container(
#                 #                     expand = True,
#                 #                     margin = 20,
#                 #                     height = 400,
#                 #                     padding = 10,
#                 #                     alignment = alignment.center,
#                 #                     col = {
#                 #                         "xs":12, "sm":6
#                 #                     },
#                 #                     content = Column(
#                 #                         expand = True,
#                 #                         horizontal_alignment = CrossAxisAlignment.CENTER,
#                 #                         alignment = MainAxisAlignment.SPACE_EVENLY,
#                 #                         controls = [
#                 #                             Text("Let's work together", size = 30, weight = FontWeight.W_900),
#                 #                             TextField(hint_text = "Email", border_radius = 10, border_color = self.color_primary, ),
#                 #                             TextField(hint_text = "Email", border_radius = 10, border_color = self.color_primary, ),
#                 #                             TextField(hint_text = "Message", border_radius = 10, border_color = self.color_primary, multiline = True, min_lines = 5, max_lines = 6 ),
#                 #                             ElevatedButton(
#                 #                                 "Send",
#                 #                                 width = 100,
#                 #                                 style = ButtonStyle(
#                 #                                     overlay_color = {"hovered" : self.color_primary},
#                 #                                     elevation = 20,
#                 #                                     shape = RoundedRectangleBorder(radius = 20),
#                 #                                     side = BorderSide(1, self.color_primary)
#                 #                                 )
#                 #                             )
                                            
#                 #                         ]
                                        
#                 #                     )
#                 #                 ),
#                 #                 Container(
#                 #                     expand = True,
#                 #                     margin = 20,
#                 #                     height = 400,
#                 #                     padding = 10,
#                 #                     alignment = alignment.center,
#                 #                     col = {
#                 #                         "xs":12, "sm":6
#                 #                     },
#                 #                     content = Column(
#                 #                         alignment = MainAxisAlignment.CENTER,
#                 #                         expand = True,
#                 #                         horizontal_alignment = CrossAxisAlignment.CENTER,
#                 #                         controls = [
#                 #                             Row(
#                 #                                 controls = [
#                 #                                     Icon(Icons.PHONE_ANDROID_OUTLINED,),
#                 #                                     Column(
#                 #                                         spacing = 0,
#                 #                                         controls = [
#                 #                                             Text("Phone", size = 13, color = self.color_primary),
#                 #                                             Text("+234-81-360-46142", size = 13, weight = FontWeight.W_900, color = self.color_primary),
                                                            
#                 #                                         ]
#                 #                                     )
#                 #                                 ]
#                 #                             ),
#                 #                             Row(
#                 #                                 controls = [
#                 #                                     Icon(Icons.EMAIL_OUTLINED,),
#                 #                                     Column(
#                 #                                         spacing = 0,
#                 #                                         controls = [
#                 #                                             Text("Email", size = 13, color = self.color_primary),
#                 #                                             Text("osiraogene@gmail.com", size = 13, weight = FontWeight.W_900, color = self.color_primary),
                                                            
#                 #                                         ]
#                 #                                     )
#                 #                                 ]
#                 #                             ),
#                 #                             Row(
#                 #                                 controls = [
#                 #                                     Icon(Icons.LOCATION_ON_OUTLINED,),
#                 #                                     Column(
#                 #                                         spacing = 0,
#                 #                                         controls = [
#                 #                                             Text("Location", size = 13, color = self.color_primary),
#                 #                                             Text("Enugu, Nigeria", size = 13, weight = FontWeight.W_900, color = self.color_primary),
                                                            
#                 #                                         ]
#                 #                                     )
#                 #                                 ]
#                 #                             ),
#                 #                             Row(
#                 #                                 alignment = MainAxisAlignment.START,
#                 #                                 spacing = 20,
#                 #                                 controls = [
#                 #                                     ElevatedButton(
#                 #                                         bgcolor = Colors.with_opacity(0.3, self.color_primary),
#                 #                                         width = 80,
#                 #                                         height = 80,
#                 #                                         on_click =  lambda e: self.open_url(2),
#                 #                                         content = Container(
#                 #                                             padding = 10,
#                 #                                             expand = True,
#                 #                                             content = Image(src = "twitter.svg", width = 80, height = 80),
#                 #                                         )
#                 #                                     ),
#                 #                                     ElevatedButton(
#                 #                                         bgcolor = Colors.with_opacity(0.3, self.color_primary),
#                 #                                         width = 80,
#                 #                                         height = 80,
#                 #                                         on_click =  lambda e: self.open_url(3),
#                 #                                         content = Container(
#                 #                                             padding = 10,
#                 #                                             expand = True,
#                 #                                             content = Image(src = "instagram_svg.svg", width = 80, height = 80),
#                 #                                         )
#                 #                                     ),
#                 #                                     ElevatedButton(
#                 #                                         bgcolor = Colors.with_opacity(0.3, self.color_primary),
#                 #                                         width = 80,
#                 #                                         height = 80,
#                 #                                         on_click =  lambda e: self.open_url(4),
#                 #                                         content = Container(
#                 #                                             padding = 10,
#                 #                                             expand = True,
#                 #                                             content = Image(src = "whatsapp.svg", width = 80, height = 80),
#                 #                                         )
#                 #                                     ),
#                 #                                 ]
#                 #                             ),
#                 #                         ]
#                 #                     )
                                    
#                 #                 )
#                 #             ]
                            
#                 #         )
#                 #     ]
#                 # )
#         )
        
#         #######  R E S U M E   F R A M E 
#         self.summary_title = Text("My Experience", size = 30, weight = FontWeight.W_900)
#         # # different containers for each reusme frames
#         # self.experience_frame = Container(
#         #     expand = True,
#         #     content = Column(
#         #         spacing = 10,
#         #         visible = True,
#         #         alignment = MainAxisAlignment.CENTER,
#         #         expand = True,
#         #         controls = [
#         #             Container(
#         #                 expand = True,
#         #                 content = Row(
#         #                     expand = True,
#         #                     alignment = MainAxisAlignment.CENTER,
#         #                     controls = [
#         #                         Container(
#         #                             expand = True,
#         #                             border_radius = 10,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             padding = 13,
#         #                             content = Column(
#         #                                 controls = [
#         #                                     Text("May of 2022 - December of 2022", size = 20, weight = FontWeight.W_900),
#         #                                     Text("The Lord is Good Computer Ltd", size = 15, weight = FontWeight.W_400),
#         #                                     # Text("Google", size = 12, font_family = self.text_fonts),
                                            
                                            
#         #                                 ]
#         #                             )
#         #                         ),
#         #                         Container(
#         #                             expand = True,
#         #                             border_radius = 10,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             padding = 13,
#         #                             content = Column(
#         #                                 controls = [
#         #                                     Text("January of 2023 - July of 2023", size = 18, weight = FontWeight.W_900),
#         #                                     Text("Not By Might Company (N.B.M.C.)", size = 12, weight = FontWeight.W_400),
#         #                                     # Text("Google", size = 12, font_family = self.text_fonts),
                                            
                                            
#         #                                 ]
#         #                             )
#         #                         )
#         #                     ]
#         #                 )
#         #             ),
#         #             Container(
#         #                 expand = True,
#         #                 content = Row(
#         #                     expand = True,
#         #                     alignment = MainAxisAlignment.CENTER,
#         #                     controls = [
#         #                         Container(
#         #                             expand = True,
#         #                             border_radius = 10,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             padding = 13,
#         #                             content = Column(
#         #                                 controls = [
#         #                                     Text(" June of 2024 - November of 2024", size = 18, weight = FontWeight.W_900),
#         #                                     Text("DesDev IT Solutions", size = 12, weight = FontWeight.W_400),
#         #                                     # Text("Google", size = 12, font_family = self.text_fonts),
                                            
                                            
#         #                                 ]
#         #                             )
#         #                         ),
#         #                         Container(
#         #                             expand = True,
#         #                             border_radius = 10,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             padding = 13,
#         #                             content = Column(
#         #                                 controls = [
#         #                                     Text("2024 - Present", size = 18, weight = FontWeight.W_900),
#         #                                     Text("", size = 12, weight = FontWeight.W_400),
#         #                                     Text("", size = 12, font_family = self.text_fonts),
                                            
                                            
#         #                                 ]
#         #                             )
#         #                         )
#         #                     ]
#         #                 )
#         #             )
#         #         ]
#         #     )
#         # )
#         # self.education_frame = Container(
#         #     expand = True,
#         #     visible = False,
#         #     content = Column(
#         #         spacing = 10,
#         #         visible = True,
#         #         alignment = MainAxisAlignment.CENTER,
#         #         expand = True,
#         #         controls = [
#         #             Container(
#         #                 expand = True,
#         #                 content = Row(
#         #                     expand = True,
#         #                     alignment = MainAxisAlignment.CENTER,
#         #                     controls = [
#         #                         Container(
#         #                             expand = True,
#         #                             border_radius = 10,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             padding = 13,
#         #                             content = Column(
#         #                                 controls = [
#         #                                     Text("2001 - 2012", size = 20, weight = FontWeight.W_900),
#         #                                     Text("Elementary Education", size = 15, weight = FontWeight.W_400),
#         #                                     Text("Pinecrest Group of Schools, Enugu", size = 12, font_family = self.text_fonts),
                                            
                                            
#         #                                 ]
#         #                             )
#         #                         ),
#         #                         Container(
#         #                             expand = True,
#         #                             border_radius = 10,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             padding = 13,
#         #                             content = Column(
#         #                                 controls = [
#         #                                     Text("2012 - 2018", size = 20, weight = FontWeight.W_900),
#         #                                     Text("Secondary School Education", size = 15, weight = FontWeight.W_400),
#         #                                     Text("Nigerian Navy Secondary School, Calabar", size = 12, font_family = self.text_fonts),
                                            
                                            
#         #                                 ]
#         #                             )
#         #                         )
#         #                     ]
#         #                 )
#         #             ),
#         #             Container(
#         #                 expand = True,
#         #                 content = Row(
#         #                     expand = True,
#         #                     alignment = MainAxisAlignment.CENTER,
#         #                     controls = [
#         #                         Container(
#         #                             expand = True,
#         #                             border_radius = 10,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             padding = 13,
#         #                             content = Column(
#         #                                 controls = [
#         #                                     Text("2018 - 2023 ", size = 18, weight = FontWeight.W_900),
#         #                                     Text("University Education", size = 12, weight = FontWeight.W_400),
#         #                                     Text("Nnamdi Azikiwe University, Awka", size = 12, font_family = self.text_fonts),
#         #                                     Text("Majored in Electronics and Computer Engineering", size = 12, font_family = self.text_fonts),
                                            
                                            
#         #                                 ]
#         #                             )
#         #                         ),
#         #                         Container(
#         #                             expand = True,
#         #                             border_radius = 10,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             padding = 13,
#         #                             content = Column(
#         #                                 controls = [
#         #                                     Text("2024 - Present", size = 18, weight = FontWeight.W_900),
#         #                                     Text("", size = 12, weight = FontWeight.W_400),
#         #                                     Text("", size = 12, font_family = self.text_fonts),
                                            
                                            
#         #                                 ]
#         #                             )
#         #                         )
#         #                     ]
#         #                 )
#         #             )
#         #         ]
#         #     )
#         # ),
#         # self.skills_frame = Container(
#         #     expand = True,
#         #     visible = False,
#         #     content = Column(
#         #         alignment = MainAxisAlignment.CENTER,
#         #         spacing = 10,
#         #         expand = True,
#         #         controls = [
#         #             Container(
#         #                 expand = True,
#         #                 content = Row(
#         #                     expand = True,
#         #                     controls = [
#         #                         Container(
#         #                             expand = True, 
#         #                             tooltip = "Pygame",
#         #                             border_radius = 10,
#         #                             padding = 15,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             content = Image(src = "/pygame_logo2.svg", )
#         #                         ),
#         #                         Container(
#         #                             expand = True, 
#         #                             tooltip = "Blender",
#         #                             border_radius = 10,
#         #                             padding = 15,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             content = Image(src = "/blender_2.svg", )
#         #                         ),
#         #                         Container(
#         #                             expand = True,
#         #                             tooltip = "Python", 
#         #                             border_radius = 10,
#         #                             padding = 15,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             content = Image(src = "/python.svg", )
#         #                         ),
#         #                     ]
#         #                 )
#         #             ),
#         #             Container(
#         #                 expand = True,
#         #                 content = Row(
#         #                     expand = True,
#         #                     controls = [
#         #                         Container(
#         #                             expand = True,
#         #                             tooltip = "Fastapi", 
#         #                             border_radius = 10,
#         #                             padding = 15,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             content = Image(src = "/fastapi_svg.svg", height = 150, width = 100 )
#         #                         ),
#         #                         Container(
#         #                             expand = True, 
#         #                             tooltip = "After Effects",
#         #                             border_radius = 10,
#         #                             padding = 15,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             content = Image(src = "/adobe_Pr.svg", expand = True,  height = 150, width = 100  )
#         #                         ),
#         #                         Container(
#         #                             expand = True,
#         #                             tooltip = "Flet", 
#         #                             border_radius = 10,
#         #                             padding = 15,
#         #                             bgcolor = Colors.with_opacity(0.2, self.color_primary),
#         #                             content = Image(src = "/flet_svg.svg", )
#         #                         ),
#         #                     ]
#         #                 )
#         #             )
#         #         ]
#         #     )
#         # )
#         # self.resume_frame = Container(
#         #     expand = True,
#         #     animate_offset = self.animation_style,
#         #     offset = transform.Offset(-2,0),
#         #     content = Column(
#         #         expand = True,
#         #         scroll = "auto",
#         #         controls = [
#         #             ResponsiveRow(
#         #                 spacing = 100,
#         #                 expand = True,
#         #                 controls = [
#         #                     Container(
#         #                         expand = True,
#         #                         margin = 20,
#         #                         height = 400,
#         #                         alignment = alignment.center,
#         #                         col = {"xs":12, "sm":6},
#         #                         content = Column(
#         #                             expand = True,
#         #                             horizontal_alignment = CrossAxisAlignment.CENTER,
#         #                             alignment = MainAxisAlignment.SPACE_EVENLY,
#         #                             controls = [
#         #                                 Text("Why hire me ?",
#         #                                      size = 30,
#         #                                      weight = FontWeight.W_900,
#         #                                      color = self.color_primary,
#         #                                      ),
#         #                                 Text("As a passionate and versatile developer, I bring a unique blend of creativity and technical expertise to the table. With hands-on experience in Python frameworks like Flet, FastAPI, and Pygame, I excel at building interactive, user-focused applications that solve real-world problems.", 
                                             
#         #                                      size = 16,
#         #                                      font_family = self.text_fonts,
                                             
#         #                                      ),
#         #                                 TextButton("Experience",
#         #                                         width = 200,
#         #                                         on_click = lambda e: self.change_resume(0),
#         #                                         style = ButtonStyle(
#         #                                             overlay_color = {"hovered" : self.color_primary},
#         #                                             shape = RoundedRectangleBorder(radius = 20),
#         #                                             side = BorderSide(1, self.color_primary),
                                                    
#         #                                         )
                                                
#         #                                         ),
#         #                                 TextButton("Education",
#         #                                         width = 200,
#         #                                         on_click = lambda e: self.change_resume(1),
#         #                                         style = ButtonStyle(
#         #                                             overlay_color = {"hovered" : self.color_primary},
#         #                                             shape = RoundedRectangleBorder(radius = 20),
#         #                                             side = BorderSide(1, self.color_primary),
                                                    
#         #                                         )
                                                
#         #                                         ),
#         #                                 TextButton("Skillset",
#         #                                         width = 200,
#         #                                         on_click = lambda e: self.change_resume(2),
#         #                                         style = ButtonStyle(
#         #                                             overlay_color = {"hovered" : self.color_primary},
#         #                                             shape = RoundedRectangleBorder(radius = 20),
#         #                                             side = BorderSide(1, self.color_primary),
                                                    
#         #                                         )
                                                
#         #                                         )
#         #                             ]
#         #                         )
#         #                     ),
#         #                     Container(
#         #                         expand = True,
#         #                         margin = 20,
#         #                         height = 400,
#         #                         col = {"xs":12, "sm":6},
#         #                         content = Column(
#         #                             expand = True,
#         #                             alignment = MainAxisAlignment.CENTER,
#         #                             horizontal_alignment = CrossAxisAlignment.CENTER,
#         #                             controls = [
#         #                                 self.summary_title,
#         #                                 # Text(value = "", size = 14),
#         #                                 Stack(
#         #                                     expand = True,
#         #                                     controls = [
#         #                                         self.experience_frame ,
#         #                                         self.education_frame ,
#         #                                         self.skills_frame ,
#         #                                     ]
#         #                                 )
#         #                             ]
#         #                         )
#         #                     )
#         #                 ]
#         #             )
#         #         ]
#         #     )
#         # )
        
        
        
#         self.controls = [ 
#             Column(
#                 expand = True,
#                 spacing = 2,
#                 controls = [
#                     Container(   #header
#                         padding = 20,
#                         content = Row(
#                             expand = True,
#                             controls = [
#                                 Container(
#                                     expand = True,
#                                     margin = margin.only(left = 20, ),
#                                     content = Text(
#                                         size = 20,
#                                         spans = [
#                                             TextSpan("Frelix", style = TextStyle(color = Colors.PURPLE_100, weight = FontWeight.W_900)),
#                                             TextSpan("Nero", style = TextStyle(color = Colors.PURPLE_400, weight = FontWeight.W_900)),
#                                             TextSpan(".", style = TextStyle(color = Colors.PURPLE_900, weight = FontWeight.W_900))
#                                         ]
#                                     )
#                                 ),
#                                 ResponsiveRow(
#                                     alignment = MainAxisAlignment.CENTER,
#                                     spacing = 0,
#                                     expand = True,
#                                     controls = [
#                                         TextButton("Start", style = ButtonStyle(color = self.color_primary), col ={
#                                             "xs":12, "sm":6, "md":3
#                                         }, on_click = lambda e: self.change_page(0) ),
#                                         TextButton("Services", style = ButtonStyle(color = self.color_primary), col ={
#                                             "xs":12, "sm":6, "md":3
#                                         }, on_click = lambda e: self.change_page(1) ),
#                                         TextButton("Resume", style = ButtonStyle(color = self.color_primary), col ={
#                                             "xs":12, "sm":6, "md":3
#                                         }, on_click = lambda e: self.change_page(2) ),
#                                         TextButton("Contact me", style = ButtonStyle(color = self.color_primary), col ={
#                                             "xs":12, "sm":6, "md":3
#                                         }, on_click = lambda e: self.change_page(3),
#                                                    )
#                                     ]
#                                 ),
#                                 Container(
#                                     width = 50,
#                                     margin = margin.only(right = 20),
#                                     content = self.switch_mode
                                    
#                                 )
                            
                            
#                             ]
                            
#                         )
#                     ),
#                     Container(          #body
#                         expand = True,
#                         content = Stack(
#                             controls = [
#                                 self.start_frame,
#                                 self.service_frame,
#                                 self.resume_frame,
#                                 self.contact_frame
#                             ]
#                         )
#                     ),
#                     Container(          #footer
#                         padding = 20,
#                         gradient = LinearGradient([self.color_primary, Colors.TRANSPARENT], rotation = 0),
#                         content = Text("Powered by Flet(Flutter) - All rights reserved",),
#                         alignment = alignment.center
#                     )
#                 ]
#             )
#         ]

    
    
#     def go_to_details(self,e):
#         if e.control.data != None :
#             self.page.session.set("images", e.control.data)
#             self.page.go('/project_image')
#         else :
#             print("error")
            
#     def build(self) :
#         self.switch_mode = IconButton(icon = icons.DARK_MODE, bgcolor = Colors.DEEP_PURPLE_900, on_click = self.dark_mode)
        
        
#         self.animation_style = animation.Animation(1000, AnimationCurve.EASE_OUT_CUBIC)
        
        
        
#         self.summary_title = Text("My Experience", size = 30, weight = FontWeight.W_900)
        
#         # different containers for each reusme frames
#         self.experience_frame = Container(
#             expand = True,
#             content = Column(
#                 spacing = 10,
#                 visible = True,
#                 alignment = MainAxisAlignment.CENTER,
#                 expand = True,
#                 controls = [
#                     Container(
#                         expand = True,
#                         content = Row(
#                             expand = True,
#                             alignment = MainAxisAlignment.CENTER,
#                             controls = [
#                                 Container(
#                                     expand = True,
#                                     border_radius = 10,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     padding = 13,
#                                     content = Column(
#                                         controls = [
#                                             Text("May of 2022 - December of 2022", size = 20, weight = FontWeight.W_900),
#                                             Text("The Lord is Good Computer Ltd", size = 15, weight = FontWeight.W_400),
#                                             # Text("Google", size = 12, font_family = self.text_fonts),
                                            
                                            
#                                         ]
#                                     )
#                                 ),
#                                 Container(
#                                     expand = True,
#                                     border_radius = 10,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     padding = 13,
#                                     content = Column(
#                                         controls = [
#                                             Text("January of 2023 - July of 2023", size = 18, weight = FontWeight.W_900),
#                                             Text("Not By Might Company (N.B.M.C.)", size = 12, weight = FontWeight.W_400),
#                                             # Text("Google", size = 12, font_family = self.text_fonts),
                                            
                                            
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     ),
#                     Container(
#                         expand = True,
#                         content = Row(
#                             expand = True,
#                             alignment = MainAxisAlignment.CENTER,
#                             controls = [
#                                 Container(
#                                     expand = True,
#                                     border_radius = 10,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     padding = 13,
#                                     content = Column(
#                                         controls = [
#                                             Text(" June of 2024 - November of 2024", size = 18, weight = FontWeight.W_900),
#                                             Text("DesDev IT Solutions", size = 12, weight = FontWeight.W_400),
#                                             # Text("Google", size = 12, font_family = self.text_fonts),
                                            
                                            
#                                         ]
#                                     )
#                                 ),
#                                 Container(
#                                     expand = True,
#                                     border_radius = 10,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     padding = 13,
#                                     content = Column(
#                                         controls = [
#                                             Text("2024 - Present", size = 18, weight = FontWeight.W_900),
#                                             Text("", size = 12, weight = FontWeight.W_400),
#                                             Text("", size = 12, font_family = self.text_fonts),
                                            
                                            
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         )
#         self.education_frame = Container(
#             expand = True,
#             visible = False,
#             content = Column(
#                 spacing = 10,
#                 visible = True,
#                 alignment = MainAxisAlignment.CENTER,
#                 expand = True,
#                 controls = [
#                     Container(
#                         expand = True,
#                         content = Row(
#                             expand = True,
#                             alignment = MainAxisAlignment.CENTER,
#                             controls = [
#                                 Container(
#                                     expand = True,
#                                     border_radius = 10,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     padding = 13,
#                                     content = Column(
#                                         controls = [
#                                             Text("2001 - 2012", size = 20, weight = FontWeight.W_900),
#                                             Text("Elementary Education", size = 15, weight = FontWeight.W_400),
#                                             Text("Pinecrest Group of Schools, Enugu", size = 12, font_family = self.text_fonts),
                                            
                                            
#                                         ]
#                                     )
#                                 ),
#                                 Container(
#                                     expand = True,
#                                     border_radius = 10,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     padding = 13,
#                                     content = Column(
#                                         controls = [
#                                             Text("2012 - 2018", size = 20, weight = FontWeight.W_900),
#                                             Text("Secondary School Education", size = 15, weight = FontWeight.W_400),
#                                             Text("Nigerian Navy Secondary School, Calabar", size = 12, font_family = self.text_fonts),
                                            
                                            
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     ),
#                     Container(
#                         expand = True,
#                         content = Row(
#                             expand = True,
#                             alignment = MainAxisAlignment.CENTER,
#                             controls = [
#                                 Container(
#                                     expand = True,
#                                     border_radius = 10,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     padding = 13,
#                                     content = Column(
#                                         controls = [
#                                             Text("2018 - 2023 ", size = 18, weight = FontWeight.W_900),
#                                             Text("University Education", size = 12, weight = FontWeight.W_400),
#                                             Text("Nnamdi Azikiwe University, Awka", size = 12, font_family = self.text_fonts),
#                                             Text("Majored in Electronics and Computer Engineering", size = 12, font_family = self.text_fonts),
                                            
                                            
#                                         ]
#                                     )
#                                 ),
#                                 Container(
#                                     expand = True,
#                                     border_radius = 10,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     padding = 13,
#                                     content = Column(
#                                         controls = [
#                                             Text("2024 - Present", size = 18, weight = FontWeight.W_900),
#                                             Text("", size = 12, weight = FontWeight.W_400),
#                                             Text("", size = 12, font_family = self.text_fonts),
                                            
                                            
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#                 ]
#             )
#         ),
#         self.skills_frame = Container(
#             expand = True,
#             visible = False,
#             content = Column(
#                 alignment = MainAxisAlignment.CENTER,
#                 spacing = 10,
#                 expand = True,
#                 controls = [
#                     Container(
#                         expand = True,
#                         content = Row(
#                             expand = True,
#                             controls = [
#                                 Container(
#                                     expand = True, 
#                                     tooltip = "Pygame",
#                                     border_radius = 10,
#                                     padding = 15,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     content = Image(src = "/pygame_logo2.svg", )
#                                 ),
#                                 Container(
#                                     expand = True, 
#                                     tooltip = "Blender",
#                                     border_radius = 10,
#                                     padding = 15,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     content = Image(src = "/blender_2.svg", )
#                                 ),
#                                 Container(
#                                     expand = True,
#                                     tooltip = "Python", 
#                                     border_radius = 10,
#                                     padding = 15,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     content = Image(src = "/python.svg", )
#                                 ),
#                             ]
#                         )
#                     ),
#                     Container(
#                         expand = True,
#                         content = Row(
#                             expand = True,
#                             controls = [
#                                 Container(
#                                     expand = True,
#                                     tooltip = "Fastapi", 
#                                     border_radius = 10,
#                                     padding = 15,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     content = Image(src = "/fastapi_svg.svg", height = 150, width = 100 )
#                                 ),
#                                 Container(
#                                     expand = True, 
#                                     tooltip = "After Effects",
#                                     border_radius = 10,
#                                     padding = 15,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     content = Image(src = "/adobe_Pr.svg", expand = True,  height = 150, width = 100  )
#                                 ),
#                                 Container(
#                                     expand = True,
#                                     tooltip = "Flet", 
#                                     border_radius = 10,
#                                     padding = 15,
#                                     bgcolor = Colors.with_opacity(0.2, self.color_primary),
#                                     content = Image(src = "/flet_svg.svg", )
#                                 ),
#                             ]
#                         )
#                     )
#                 ]
#             )
#         )
#         self.resume_frame = Container(
#             expand = True,
#             animate_offset = self.animation_style,
#             offset = transform.Offset(-2,0),
#             content = Column(
#                 expand = True,
#                 scroll = "auto",
#                 controls = [
#                     ResponsiveRow(
#                         spacing = 100,
#                         expand = True,
#                         controls = [
#                             Container(
#                                 expand = True,
#                                 margin = 20,
#                                 height = 400,
#                                 alignment = alignment.center,
#                                 col = {"xs":12, "sm":6},
#                                 content = Column(
#                                     expand = True,
#                                     horizontal_alignment = CrossAxisAlignment.CENTER,
#                                     alignment = MainAxisAlignment.SPACE_EVENLY,
#                                     controls = [
#                                         Text("Why hire me ?",
#                                              size = 30,
#                                              weight = FontWeight.W_900,
#                                              color = self.color_primary,
#                                              ),
#                                         Text("As a passionate and versatile developer, I bring a unique blend of creativity and technical expertise to the table. With hands-on experience in Python frameworks like Flet, FastAPI, and Pygame, I excel at building interactive, user-focused applications that solve real-world problems.", 
                                             
#                                              size = 16,
#                                              font_family = self.text_fonts,
                                             
#                                              ),
#                                         TextButton("Experience",
#                                                 width = 200,
#                                                 on_click = lambda e: self.change_resume(0),
#                                                 style = ButtonStyle(
#                                                     overlay_color = {"hovered" : self.color_primary},
#                                                     shape = RoundedRectangleBorder(radius = 20),
#                                                     side = BorderSide(1, self.color_primary),
                                                    
#                                                 )
                                                
#                                                 ),
#                                         TextButton("Education",
#                                                 width = 200,
#                                                 on_click = lambda e: self.change_resume(1),
#                                                 style = ButtonStyle(
#                                                     overlay_color = {"hovered" : self.color_primary},
#                                                     shape = RoundedRectangleBorder(radius = 20),
#                                                     side = BorderSide(1, self.color_primary),
                                                    
#                                                 )
                                                
#                                                 ),
#                                         TextButton("Skillset",
#                                                 width = 200,
#                                                 on_click = lambda e: self.change_resume(2),
#                                                 style = ButtonStyle(
#                                                     overlay_color = {"hovered" : self.color_primary},
#                                                     shape = RoundedRectangleBorder(radius = 20),
#                                                     side = BorderSide(1, self.color_primary),
                                                    
#                                                 )
                                                
#                                                 )
#                                     ]
#                                 )
#                             ),
#                             Container(
#                                 expand = True,
#                                 margin = 20,
#                                 height = 400,
#                                 col = {"xs":12, "sm":6},
#                                 content = Column(
#                                     expand = True,
#                                     alignment = MainAxisAlignment.CENTER,
#                                     horizontal_alignment = CrossAxisAlignment.CENTER,
#                                     controls = [
#                                         self.summary_title,
#                                         # Text(value = "", size = 14),
#                                         Stack(
#                                             expand = True,
#                                             controls = [
#                                                 self.experience_frame ,
#                                                 self.education_frame ,
#                                                 self.skills_frame ,
#                                             ]
#                                         )
#                                     ]
#                                 )
#                             )
#                         ]
#                     )
#                 ]
#             )
#         )
#         self.contact_frame = Container(
#             expand = True,
#             animate_offset = self.animation_style,
#             offset = transform.Offset(-2,0),
#             content = Column(
#                 scroll = "auto",
#                 expand = True,
#                 controls = [
#                     ResponsiveRow(
#                         expand = True,
#                         controls = [
#                             Container(
#                                 expand = True,
#                                 margin = 20,
#                                 height = 400,
#                                 padding = 10,
#                                 alignment = alignment.center,
#                                 col = {
#                                     "xs":12, "sm":6
#                                 },
#                                 content = Column(
#                                     expand = True,
#                                     horizontal_alignment = CrossAxisAlignment.CENTER,
#                                     alignment = MainAxisAlignment.SPACE_EVENLY,
#                                     controls = [
#                                         Text("Let's work together", size = 30, weight = FontWeight.W_900),
#                                         TextField(hint_text = "Email", border_radius = 10, border_color = self.color_primary, ),
#                                         TextField(hint_text = "Email", border_radius = 10, border_color = self.color_primary, ),
#                                         TextField(hint_text = "Message", border_radius = 10, border_color = self.color_primary, multiline = True, min_lines = 5, max_lines = 6 ),
#                                         ElevatedButton(
#                                             "Send",
#                                             width = 100,
#                                             style = ButtonStyle(
#                                                 overlay_color = {"hovered" : self.color_primary},
#                                                 elevation = 20,
#                                                 shape = RoundedRectangleBorder(radius = 20),
#                                                 side = BorderSide(1, self.color_primary)
#                                             )
#                                         )
                                        
#                                     ]
                                    
#                                 )
#                             ),
#                             Container(
#                                 expand = True,
#                                 margin = 20,
#                                 height = 400,
#                                 padding = 10,
#                                 alignment = alignment.center,
#                                 col = {
#                                     "xs":12, "sm":6
#                                 },
#                                 content = Column(
#                                     alignment = MainAxisAlignment.CENTER,
#                                     expand = True,
#                                     horizontal_alignment = CrossAxisAlignment.CENTER,
#                                     controls = [
#                                         Row(
#                                             controls = [
#                                                 Icon(Icons.PHONE_ANDROID_OUTLINED,),
#                                                 Column(
#                                                     spacing = 0,
#                                                     controls = [
#                                                         Text("Phone", size = 13, color = self.color_primary),
#                                                         Text("+234-81-360-46142", size = 13, weight = FontWeight.W_900, color = self.color_primary),
                                                        
#                                                     ]
#                                                 )
#                                             ]
#                                         ),
#                                         Row(
#                                             controls = [
#                                                 Icon(Icons.EMAIL_OUTLINED,),
#                                                 Column(
#                                                     spacing = 0,
#                                                     controls = [
#                                                         Text("Email", size = 13, color = self.color_primary),
#                                                         Text("osiraogene@gmail.com", size = 13, weight = FontWeight.W_900, color = self.color_primary),
                                                        
#                                                     ]
#                                                 )
#                                             ]
#                                         ),
#                                         Row(
#                                             controls = [
#                                                 Icon(Icons.LOCATION_ON_OUTLINED,),
#                                                 Column(
#                                                     spacing = 0,
#                                                     controls = [
#                                                         Text("Location", size = 13, color = self.color_primary),
#                                                         Text("Enugu, Nigeria", size = 13, weight = FontWeight.W_900, color = self.color_primary),
                                                        
#                                                     ]
#                                                 )
#                                             ]
#                                         ),
#                                         Row(
#                                             alignment = MainAxisAlignment.START,
#                                             spacing = 20,
#                                             controls = [
#                                                 ElevatedButton(
#                                                     bgcolor = Colors.with_opacity(0.3, self.color_primary),
#                                                     width = 80,
#                                                     height = 80,
#                                                     on_click =  lambda e: self.open_url(2),
#                                                     content = Container(
#                                                         padding = 10,
#                                                         expand = True,
#                                                         content = Image(src = "twitter.svg", width = 80, height = 80),
#                                                     )
#                                                 ),
#                                                 ElevatedButton(
#                                                     bgcolor = Colors.with_opacity(0.3, self.color_primary),
#                                                     width = 80,
#                                                     height = 80,
#                                                     on_click =  lambda e: self.open_url(3),
#                                                     content = Container(
#                                                         padding = 10,
#                                                         expand = True,
#                                                         content = Image(src = "instagram_svg.svg", width = 80, height = 80),
#                                                     )
#                                                 ),
#                                                 ElevatedButton(
#                                                     bgcolor = Colors.with_opacity(0.3, self.color_primary),
#                                                     width = 80,
#                                                     height = 80,
#                                                     on_click =  lambda e: self.open_url(4),
#                                                     content = Container(
#                                                         padding = 10,
#                                                         expand = True,
#                                                         content = Image(src = "whatsapp.svg", width = 80, height = 80),
#                                                     )
#                                                 ),
#                                             ]
#                                         ),
#                                     ]
#                                 )
                                
#                             )
#                         ]
                        
#                     )
#                 ]
#             )
#         )
        
#         # self.page.add(self.content,)
        
#     def change_page(self,e) :
#         self.start_frame.offset.x = -2
#         self.service_frame.offset.x = -2
#         self.resume_frame.offset.x = -2
#         self.contact_frame.offset.x = 0
        
#         if e == 0 :
#             self.start_frame.offset.x = 0
#         if e == 1 :
#             self.service_frame.offset.x = 0
#         if e == 2 :
#             self.resume_frame.offset.x = 0
#         if e == 3 :
#             print("C O N T A C T")
#             self.contact_frame.offset.x = 0
        
#         self.start_frame.update()
#         self.service_frame.update()
#         self.resume_frame.update()
#         self.contact_frame.update()


    
#     def dark_mode(self,e) :
#         if e.control.value == False :
#             # self.switch_mode.icon = Icons.LIGHT_MODE
#             self.page.theme_mode = "dark"
#             print("light mode")
#         else : 
#             self.page.theme_mode = "light"
#             print("theme changed")
#         self.page.update()
        
#     def change_resume(self,e) :
#         self.experience_frame.visible = False
#         self.education_frame.visible = False
#         self.skills_frame.visible = False
        
#         if e == 0 :
#             self.experience_frame.visible = True
#             self.summary_title.value = "My Experience"
#         elif e == 1 : 
#             self.education_frame.visible = True
#             self.summary_title.value = "My Educational Level"
#         elif e == 2 :
#             self.skills_frame.visible = True
#             self.summary_title.value = "My Skillset"
            
#         self.page.update()
        
#     def open_url(self,e):
#         if e == 0 :
#             self.page.launch_url("https://www.linkedin.com/in/osita-felix-368a9b175?trk=contact-info")
#             # webbrowser.open("https://www.linkedin.com/in/osita-felix-368a9b175?trk=contact-info")
#         elif e == 1:
#             self.page.launch_url("https://github.com/frelixnero")
#         elif e == 2 :
#             self.page.launch_url("https://x.com/Frelixnero?t=B63-W-Tmvwx3PGMbM9HPWg&s=08")
#         elif e == 3 :
#             self.page.launch_url("https://www.instagram.com/frelixnero?igsh=YzljYTk1ODg3Zg==")
#         elif e == 4 :
#             self.page.launch_url("https://wa.me/qr/A3MPE6MABE73F1")
#         elif e == 5 :
#             self.page.launch_url("https://github.com/frelixnero/my_fastapi_backend")
#         elif e == 6 :
#             self.page.launch_url("https://github.com/frelixnero/Paystack_Verfication_with_FastApi_for_Flutter_apps")
            
# def main(page : Page) :
    
#     def router (route) :
#         page.views.clear()
        
#         if page.route == "/portfolio" :
#             portfolio = Portfolio(page)
#             page.views.append(portfolio)
            
#         if page.route == "/project_image" :
#             project_image = ProjectImage(page)
#             page.views.append(project_image)
            
#         page.update()
            
        
        
#     page.on_route_change = router
#     page.go("/portfolio")
#     page.update()
    
# # # Start the Flet app
# app(target=main, view = WEB_BROWSER, assets_dir = "assets")

# # app(target = lambda page : Portfolio(page), view = WEB_BROWSER, assets_dir = "assets")
