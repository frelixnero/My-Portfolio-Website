from flet import *
import webbrowser


class Portfolio(Container) :
    def __init__(self, page : Page):
        super().__init__()
        
        self.page = page
        self.page.padding = 0
        self.page.fonts = {"Starjhol": "../assets/Starjhol.ttf"}
        self.text_fonts = "Tahoma"
        
        self.color_primary = Colors.PURPLE_400
        self.build()
        
    def build(self) :
        self.switch_mode = IconButton(icon = icons.DARK_MODE, bgcolor = Colors.DEEP_PURPLE_900, on_click = self.dark_mode)
        
        
        self.animation_style = animation.Animation(1000, AnimationCurve.EASE_OUT_CUBIC)
        
        self.start_frame = Container(
            expand = True,
            # bgcolor = "grey",
            animate_offset = self.animation_style,
            offset = transform.Offset(0,0),
            content = Row(
                expand = True,
                controls = [
                    Container(
                        margin = 20,
                        expand = True,
                        content = Column(
                            alignment = MainAxisAlignment.CENTER,
                            horizontal_alignment = CrossAxisAlignment.CENTER,
                            controls = [
                                Text("Hello", size = 30, weight = FontWeight.W_800),
                                Text("I'm Osita", size = 30, weight = FontWeight.W_800, color = self.color_primary),
                                Row(
                                    expand = True,
                                    spacing = 0,
                                    controls = [
                                        TextButton("Download CV",

                                                   style = ButtonStyle(shape = RoundedRectangleBorder(radius = 20),
                                                                       side = BorderSide(1, self.color_primary)
                                                                       , overlay_color = {"hovered" : self.color_primary})
                                                   ),
                                        ElevatedButton( content = Image(
                                            src =   "/linkedin.png",
                                            fit = ImageFit.COVER, width = 20, 
                                        ),
                                            data = "https://www.linkedin.com/in/osita-felix-368a9b175?trk=contact-info",
                                            on_click = self.open_url,
                                         style = ButtonStyle(side = BorderSide(1, self.color_primary),shape = CircleBorder(),
                                                             overlay_color = {"hovered" : self.color_primary}),           
                                            height = 40,                                        
                                        ),
                                        ElevatedButton( content = Image(
                                            src = "/github.png",
                                            fit = ImageFit.COVER, width = 20, 
                                        ),
                                            data = "https://github.com/frelixnero",
                                            on_click = self.open_url,
                                         style = ButtonStyle(side = BorderSide(1, self.color_primary),shape = CircleBorder(),
                                                             overlay_color = {"hovered" : self.color_primary}),           
                                            height = 40,                                        
                                        ),
                                        ElevatedButton( content = Image(
                                            src = "/youtube.png",
                                            fit = ImageFit.COVER, width = 20, 
                                        ),
                                         style = ButtonStyle(side = BorderSide(1, self.color_primary),shape = CircleBorder(),
                                                             overlay_color = {"hovered" : self.color_primary}),           
                                            height = 40,                                        
                                        )
                                    ]
                                )
                            ]
                        )
                    ),
                    
                    Container(
                        expand = True,
                        shape = BoxShape.CIRCLE,
                        clip_behavior = ClipBehavior.ANTI_ALIAS,
                        margin = 50,
                        shadow = BoxShadow(
                            spread_radius = 30,
                            blur_radius = 30,
                            color = self.color_primary
                            ),
                        content = Image(
                            src = "/foto.jpg"
                        )
                    )
                ]
            )
        )
        self.service_frame = Container(
            expand = True,
            animate_offset = self.animation_style,
            offset = transform.Offset(-2,0),
            content = Column(
                scroll = "auto",
                expand = True,
                controls = [
                    ResponsiveRow(
                        expand = True,
                        spacing = 20,
                        controls = [
                            Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 200,
                                      padding = 10,
                                      border = Border(bottom = BorderSide(2, self.color_primary)),
                                      content = Column(
                                          controls = [
                                            Row(
                                              expand = True,
                                              alignment = MainAxisAlignment.SPACE_BETWEEN,
                                              vertical_alignment = CrossAxisAlignment.CENTER,
                                              spacing = 20,
                                              controls = [
                                                  Text("01", size = 30, weight = FontWeight.W_900,
                                                       font_family = "Starjhol"),
                                                  IconButton(icon = Icons.ARROW_OUTWARD,
                                                             style = ButtonStyle(
                                                                 bgcolor = self.color_primary,
                                                                 
                                                             ),
                                                             
                                                             )
                                              ]
                                          ),


                                            Text("Work 01", size = 30, weight = FontWeight.W_900),
                                            
                                            Text(size = 12, value = "I'm a python developer with strong expertise in frontend development using tools like Flet and a growing capability in backend systems such as FastAPI. My work spans across web applications, user interface design, and app logic, showcasing proficiency in frameworks that blend Python with interactive, dynamic user experiences.",
                                                 font_family = self.text_fonts)
                                          ]
                                          
                                      )
                                      ),
                            Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 200,
                                      padding = 10,
                                      border = Border(bottom = BorderSide(2, self.color_primary)),
                                      content = Column(
                                          controls = [
                                            Row(
                                              expand = True,
                                              alignment = MainAxisAlignment.SPACE_BETWEEN,
                                              vertical_alignment = CrossAxisAlignment.CENTER,
                                              spacing = 20,
                                              controls = [
                                                  Text("02", size = 30, weight = FontWeight.W_900,
                                                       font_family = "Starjhol"),
                                                  IconButton(icon = Icons.ARROW_OUTWARD,
                                                             style = ButtonStyle(
                                                                 bgcolor = self.color_primary,
                                                                 
                                                             ),
                                                             
                                                             )
                                              ]
                                          ),
                                            Text("Work 02", size = 30, weight = FontWeight.W_900),
                                            
                                            Text(size = 12, value = "As a Flet developer, I specialize in creating dynamic, cross-platform web and desktop applications with responsive UI/UX, seamless integration of interactive components, and optimized performance tailored to your business needs",
                                                 font_family = self.text_fonts)
                                          ]
                                          
                                      )
                                      ),
                            Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 200,
                                      padding = 10,
                                      border = Border(bottom = BorderSide(2, self.color_primary)),
                                      content = Column(
                                          controls = [
                                            Row(
                                              expand = True,
                                              alignment = MainAxisAlignment.SPACE_BETWEEN,
                                              vertical_alignment = CrossAxisAlignment.CENTER,
                                              spacing = 20,
                                              controls = [
                                                  Text("03", size = 30, weight = FontWeight.W_900,
                                                       font_family = "Starjhol"),
                                                  IconButton(icon = Icons.ARROW_OUTWARD,
                                                             style = ButtonStyle(
                                                                 bgcolor = self.color_primary,
                                                                 
                                                             ),
                                                             
                                                             )
                                              ]
                                          ),


                                            Text("Work 03", size = 30, weight = FontWeight.W_900),
                                            
                                            Text(size = 12, value = "As a FastAPI developer, I specialize in creating high-performance, scalable RESTful APIs and robust backend systems to support web and mobile applications. My expertise includes integrating APIs with third-party services, implementing secure authentication systems, and designing microservices architectures. I also provide real-time functionality, thorough testing, and interactive API documentation using OpenAPI standards.",
                                                 font_family = self.text_fonts)
                                          ]
                                          
                                      )
                                      ),
                            Container(margin = 20, expand = True, col = {"md":12,"lg":6}, height = 200,
                                      padding = 10,
                                      border = Border(bottom = BorderSide(2, self.color_primary)),
                                      content = Column(
                                          controls = [
                                            Row(
                                              expand = True,
                                              alignment = MainAxisAlignment.SPACE_BETWEEN,
                                              vertical_alignment = CrossAxisAlignment.CENTER,
                                              spacing = 20,
                                              controls = [
                                                  Text("04", size = 30, weight = FontWeight.W_900,
                                                       font_family = "Starjhol"),
                                                  IconButton(icon = Icons.ARROW_OUTWARD,
                                                             style = ButtonStyle(
                                                                 bgcolor = self.color_primary,
                                                                 
                                                             ),
                                                             
                                                             )
                                              ]
                                          ),
                                            Text("Work 04", size = 30, weight = FontWeight.W_900),
                                            
                                            Text(size = 12, value = "I'm a python developer with strong expertise in frontend development using tools like Flet and a growing capability in backend systems such as FastAPI. My work spans across web applications, user interface design, and app logic, showcasing proficiency in frameworks that blend Python with interactive, dynamic user experiences.",
                                                 font_family = self.text_fonts)
                                          ]
                                          
                                      )
                                      ),
                        ]
                    )
                ]
            )
        )
        self.summary_title = Text("My Experience", size = 30, weight = FontWeight.W_900)
        
        # different containers for each reusme frames
        self.experience_frame = Container(
            expand = True,
            content = Column(
                spacing = 10,
                visible = True,
                alignment = MainAxisAlignment.CENTER,
                expand = True,
                controls = [
                    Container(
                        expand = True,
                        content = Row(
                            expand = True,
                            alignment = MainAxisAlignment.CENTER,
                            controls = [
                                Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = Column(
                                        controls = [
                                            Text("May of 2022 - December of 2022", size = 20, weight = FontWeight.W_900),
                                            Text("The Lord is Good Computer Ltd", size = 15, weight = FontWeight.W_400),
                                            # Text("Google", size = 12, font_family = self.text_fonts),
                                            
                                            
                                        ]
                                    )
                                ),
                                Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = Column(
                                        controls = [
                                            Text("January of 2023 - July of 2023", size = 18, weight = FontWeight.W_900),
                                            Text("Not By Might Company (N.B.M.C.)", size = 12, weight = FontWeight.W_400),
                                            # Text("Google", size = 12, font_family = self.text_fonts),
                                            
                                            
                                        ]
                                    )
                                )
                            ]
                        )
                    ),
                    Container(
                        expand = True,
                        content = Row(
                            expand = True,
                            alignment = MainAxisAlignment.CENTER,
                            controls = [
                                Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = Column(
                                        controls = [
                                            Text(" June of 2024 - November of 2024", size = 18, weight = FontWeight.W_900),
                                            Text("DesDev IT Solutions", size = 12, weight = FontWeight.W_400),
                                            # Text("Google", size = 12, font_family = self.text_fonts),
                                            
                                            
                                        ]
                                    )
                                ),
                                Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = Column(
                                        controls = [
                                            Text("2024 - Present", size = 18, weight = FontWeight.W_900),
                                            Text("", size = 12, weight = FontWeight.W_400),
                                            Text("", size = 12, font_family = self.text_fonts),
                                            
                                            
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.education_frame = Container(
            expand = True,
            visible = False,
            content = Column(
                spacing = 10,
                visible = True,
                alignment = MainAxisAlignment.CENTER,
                expand = True,
                controls = [
                    Container(
                        expand = True,
                        content = Row(
                            expand = True,
                            alignment = MainAxisAlignment.CENTER,
                            controls = [
                                Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = Column(
                                        controls = [
                                            Text("2001 - 2012", size = 20, weight = FontWeight.W_900),
                                            Text("Elementary Education", size = 15, weight = FontWeight.W_400),
                                            Text("Pinecrest Group of Schools, Enugu", size = 12, font_family = self.text_fonts),
                                            
                                            
                                        ]
                                    )
                                ),
                                Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = Column(
                                        controls = [
                                            Text("2012 - 2018", size = 20, weight = FontWeight.W_900),
                                            Text("Secondary School Education", size = 15, weight = FontWeight.W_400),
                                            Text("Nigerian Navy Secondary School, Calabar", size = 12, font_family = self.text_fonts),
                                            
                                            
                                        ]
                                    )
                                )
                            ]
                        )
                    ),
                    Container(
                        expand = True,
                        content = Row(
                            expand = True,
                            alignment = MainAxisAlignment.CENTER,
                            controls = [
                                Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = Column(
                                        controls = [
                                            Text("2018 - 2023 ", size = 18, weight = FontWeight.W_900),
                                            Text("University Education", size = 12, weight = FontWeight.W_400),
                                            Text("Nnamdi Azikiwe University, Awka", size = 12, font_family = self.text_fonts),
                                            Text("Majored in Electronics and Computer Engineering", size = 12, font_family = self.text_fonts),
                                            
                                            
                                        ]
                                    )
                                ),
                                Container(
                                    expand = True,
                                    border_radius = 10,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    padding = 13,
                                    content = Column(
                                        controls = [
                                            Text("2024 - Present", size = 18, weight = FontWeight.W_900),
                                            Text("", size = 12, weight = FontWeight.W_400),
                                            Text("", size = 12, font_family = self.text_fonts),
                                            
                                            
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.skills_frame = Container(
            expand = True,
            visible = False,
            content = Column(
                alignment = MainAxisAlignment.CENTER,
                spacing = 10,
                expand = True,
                controls = [
                    Container(
                        expand = True,
                        content = Row(
                            expand = True,
                            controls = [
                                Container(
                                    expand = True, 
                                    tooltip = "Pygame",
                                    border_radius = 10,
                                    padding = 15,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    content = Image(src = "/pygame_logo2.svg", )
                                ),
                                Container(
                                    expand = True, 
                                    tooltip = "Blender",
                                    border_radius = 10,
                                    padding = 15,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    content = Image(src = "/blender_2.svg", )
                                ),
                                Container(
                                    expand = True,
                                    tooltip = "Python", 
                                    border_radius = 10,
                                    padding = 15,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    content = Image(src = "/python.svg", )
                                ),
                            ]
                        )
                    ),
                    Container(
                        expand = True,
                        content = Row(
                            expand = True,
                            controls = [
                                Container(
                                    expand = True,
                                    tooltip = "Fastapi", 
                                    border_radius = 10,
                                    padding = 15,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    content = Image(src = "/fastapi_svg.svg", height = 150, width = 100 )
                                ),
                                Container(
                                    expand = True, 
                                    tooltip = "After Effects",
                                    border_radius = 10,
                                    padding = 15,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    content = Image(src = "/adobe_Pr.svg", expand = True,  height = 150, width = 100  )
                                ),
                                Container(
                                    expand = True,
                                    tooltip = "Flet", 
                                    border_radius = 10,
                                    padding = 15,
                                    bgcolor = Colors.with_opacity(0.2, self.color_primary),
                                    content = Image(src = "/flet_svg.svg", )
                                ),
                            ]
                        )
                    )
                ]
            )
        )
        self.resume_frame = Container(
            expand = True,
            animate_offset = self.animation_style,
            offset = transform.Offset(-2,0),
            content = Column(
                expand = True,
                scroll = "auto",
                controls = [
                    ResponsiveRow(
                        spacing = 100,
                        expand = True,
                        controls = [
                            Container(
                                expand = True,
                                margin = 20,
                                height = 400,
                                alignment = alignment.center,
                                col = {"xs":12, "sm":6},
                                content = Column(
                                    expand = True,
                                    horizontal_alignment = CrossAxisAlignment.CENTER,
                                    alignment = MainAxisAlignment.SPACE_EVENLY,
                                    controls = [
                                        Text("Why hire me ?",
                                             size = 30,
                                             weight = FontWeight.W_900,
                                             color = self.color_primary,
                                             ),
                                        Text("As a passionate and versatile developer, I bring a unique blend of creativity and technical expertise to the table. With hands-on experience in Python frameworks like Flet, FastAPI, and Pygame, I excel at building interactive, user-focused applications that solve real-world problems.", 
                                             
                                             size = 16,
                                             font_family = self.text_fonts,
                                             
                                             ),
                                        TextButton("Experience",
                                                width = 200,
                                                on_click = lambda e: self.change_resume(0),
                                                style = ButtonStyle(
                                                    overlay_color = {"hovered" : self.color_primary},
                                                    shape = RoundedRectangleBorder(radius = 20),
                                                    side = BorderSide(1, self.color_primary),
                                                    
                                                )
                                                
                                                ),
                                        TextButton("Education",
                                                width = 200,
                                                on_click = lambda e: self.change_resume(1),
                                                style = ButtonStyle(
                                                    overlay_color = {"hovered" : self.color_primary},
                                                    shape = RoundedRectangleBorder(radius = 20),
                                                    side = BorderSide(1, self.color_primary),
                                                    
                                                )
                                                
                                                ),
                                        TextButton("Skillset",
                                                width = 200,
                                                on_click = lambda e: self.change_resume(2),
                                                style = ButtonStyle(
                                                    overlay_color = {"hovered" : self.color_primary},
                                                    shape = RoundedRectangleBorder(radius = 20),
                                                    side = BorderSide(1, self.color_primary),
                                                    
                                                )
                                                
                                                )
                                    ]
                                )
                            ),
                            Container(
                                expand = True,
                                margin = 20,
                                height = 400,
                                col = {"xs":12, "sm":6},
                                content = Column(
                                    expand = True,
                                    alignment = MainAxisAlignment.CENTER,
                                    horizontal_alignment = CrossAxisAlignment.CENTER,
                                    controls = [
                                        self.summary_title,
                                        # Text(value = "", size = 14),
                                        Stack(
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
        self.contact_frame = Container(
            expand = True,
            # bgcolor = "pink",
            animate_offset = self.animation_style,
            offset = transform.Offset(-2,0),
            content = Column(
                scroll = "auto",
                expand = True,
                controls = [
                    ResponsiveRow(
                        expand = True,
                        controls = [
                            Container(
                                expand = True,
                                margin = 20,
                                height = 400,
                                padding = 10,
                                alignment = alignment.center,
                                col = {
                                    "xs":12, "sm":6
                                },
                                content = Column(
                                    expand = True,
                                    horizontal_alignment = CrossAxisAlignment.CENTER,
                                    alignment = MainAxisAlignment.SPACE_EVENLY,
                                    controls = [
                                        Text("Let's work together", size = 30, weight = FontWeight.W_900),
                                        TextField(hint_text = "Email", border_radius = 10, border_color = self.color_primary, ),
                                        TextField(hint_text = "Email", border_radius = 10, border_color = self.color_primary, ),
                                        TextField(hint_text = "Message", border_radius = 10, border_color = self.color_primary, multiline = True, min_lines = 5, max_lines = 6 ),
                                        ElevatedButton(
                                            "Send",
                                            width = 100,
                                            style = ButtonStyle(
                                                overlay_color = {"hovered" : self.color_primary},
                                                elevation = 20,
                                                shape = RoundedRectangleBorder(radius = 20),
                                                side = BorderSide(1, self.color_primary)
                                            )
                                        )
                                        
                                    ]
                                    
                                )
                            ),
                            Container(
                                expand = True,
                                margin = 20,
                                height = 400,
                                padding = 10,
                                alignment = alignment.center,
                                col = {
                                    "xs":12, "sm":6
                                },
                                content = Column(
                                    alignment = MainAxisAlignment.CENTER,
                                    expand = True,
                                    horizontal_alignment = CrossAxisAlignment.CENTER,
                                    controls = [
                                        Row(
                                            controls = [
                                                Icon(Icons.PHONE_ANDROID_OUTLINED,),
                                                Column(
                                                    spacing = 0,
                                                    controls = [
                                                        Text("Phone", size = 13, color = self.color_primary),
                                                        Text("+234-81-360-46142", size = 13, weight = FontWeight.W_900, color = self.color_primary),
                                                        
                                                    ]
                                                )
                                            ]
                                        ),
                                        Row(
                                            controls = [
                                                Icon(Icons.EMAIL_OUTLINED,),
                                                Column(
                                                    spacing = 0,
                                                    controls = [
                                                        Text("Email", size = 13, color = self.color_primary),
                                                        Text("osiraogene@gmail.com", size = 13, weight = FontWeight.W_900, color = self.color_primary),
                                                        
                                                    ]
                                                )
                                            ]
                                        ),
                                        Row(
                                            controls = [
                                                Icon(Icons.LOCATION_ON_OUTLINED,),
                                                Column(
                                                    spacing = 0,
                                                    controls = [
                                                        Text("Location", size = 13, color = self.color_primary),
                                                        Text("Enugu, Nigeria", size = 13, weight = FontWeight.W_900, color = self.color_primary),
                                                        
                                                    ]
                                                )
                                            ]
                                        ),
                                        Row(
                                            alignment = MainAxisAlignment.START,
                                            spacing = 20,
                                            controls = [
                                                Container(
                                                    padding = 10,
                                                    bgcolor = Colors.with_opacity(0.3, self.color_primary),
                                                    width = 80,
                                                    height = 80,
                                                    on_click=self.open_url,
                                                    data = "https://x.com/Frelixnero?t=B63-W-Tmvwx3PGMbM9HPWg&s=08",
                                                    content = Image(src = "twitter.svg"),
                                                ),
                                                Container(
                                                    padding = 10,
                                                    bgcolor = Colors.with_opacity(0.3, self.color_primary),
                                                    width = 80,
                                                    height = 80,
                                                    on_click = self.open_url,
                                                    data = "https://www.instagram.com/frelixnero?igsh=YzljYTk1ODg3Zg==",
                                                    content = Image(src = "instagram_svg.svg"),
                                                ),
                                                Container(
                                                    padding = 10,
                                                    bgcolor = Colors.with_opacity(0.3, self.color_primary),
                                                    width = 80,
                                                    height = 80,
                                                    on_click = self.open_url,
                                                    data = "https://wa.me/qr/A3MPE6MABE73F1",
                                                    content = Image(src = "whatsapp.svg"),
                                                )
                                                
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
        self.content = Column(
            expand = True,
            spacing = 2,
            controls = [
                Container(   #header
                    padding = 20,
                    content = Row(
                        expand = True,
                        controls = [
                            Container(
                                expand = True,
                                margin = margin.only(left = 20, ),
                                content = Text(
                                    size = 20,
                                    spans = [
                                        TextSpan("Frelix", style = TextStyle(color = Colors.PURPLE_100, weight = FontWeight.W_900)),
                                        TextSpan("Nero", style = TextStyle(color = Colors.PURPLE_400, weight = FontWeight.W_900)),
                                        TextSpan(".", style = TextStyle(color = Colors.PURPLE_900, weight = FontWeight.W_900))
                                    ]
                                )
                            ),
                            ResponsiveRow(
                                alignment = MainAxisAlignment.CENTER,
                                spacing = 0,
                                expand = True,
                                controls = [
                                    TextButton("Start", style = ButtonStyle(color = self.color_primary), col ={
                                        "xs":12, "sm":6, "md":3
                                    }, on_click = lambda e: self.change_page(0) ),
                                    TextButton("Services", style = ButtonStyle(color = self.color_primary), col ={
                                        "xs":12, "sm":6, "md":3
                                    }, on_click = lambda e: self.change_page(1) ),
                                    TextButton("Resume", style = ButtonStyle(color = self.color_primary), col ={
                                        "xs":12, "sm":6, "md":3
                                    }, on_click = lambda e: self.change_page(2) ),
                                    TextButton("Contact me", style = ButtonStyle(color = self.color_primary), col ={
                                        "xs":12, "sm":6, "md":3
                                    }, on_click = lambda e: self.change_page(3) )
                                ]
                            ),
                            Container(
                                width = 50,
                                margin = margin.only(right = 20),
                                content = self.switch_mode
                                
                            )
                        
                        
                        ]
                        
                    )
                ),
                Container(          #body
                    expand = True,
                    content = Stack(
                        controls = [
                            self.start_frame,
                            self.service_frame,
                            self.resume_frame,
                            self.contact_frame
                        ]
                    )
                ),
                Container(          #footer
                    padding = 20,
                    gradient = LinearGradient([self.color_primary, Colors.TRANSPARENT], rotation = 0),
                    content = Text("Powered by Flet(Flutter) - All rights reserved",),
                    alignment = alignment.center
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
        print(e)
    
    def dark_mode(self,e) :
        if e.control.icon == "dark_mode" :
            self.switch_mode.icon = Icons.LIGHT_MODE
            self.page.theme_mode = "light"
            print("light mode")
        else : 
            self.switch_mode.icon = Icons.DARK_MODE
            self.page.theme_mode = "dark"
            print("theme changed")
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
        webbrowser.open(e.control.data)
    
        
def main(page: Page):
    pass


app(target = lambda page : Portfolio(page), view = WEB_BROWSER, assets_dir = "assets")
