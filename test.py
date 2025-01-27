from flet import *



color_primary = Colors.PURPLE_400




self_content = Column(
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
                                    TextButton("Start", style = ButtonStyle(color = color_primary), col ={
                                        "xs":12, "sm":6, "md":3
                                    }, on_click = lambda e: change_page(0) ),
                                    TextButton("Services", style = ButtonStyle(color = color_primary), col ={
                                        "xs":12, "sm":6, "md":3
                                    }, on_click = lambda e: change_page(1) ),
                                    TextButton("Resume", style = ButtonStyle(color = color_primary), col ={
                                        "xs":12, "sm":6, "md":3
                                    }, on_click = lambda e: change_page(2) ),
                                    TextButton("Contact me", style = ButtonStyle(color = color_primary), col ={
                                        "xs":12, "sm":6, "md":3
                                    }, on_click = lambda e: change_page(3) )
                                ]
                            ),
                            
                        
                            Container(          #footer
                                padding = 20,
                                gradient = LinearGradient([color_primary, Colors.TRANSPARENT], rotation = 0),
                                content = Text("Copyright 2024 FrelixNero - All rights reserved",),
                                alignment = alignment.center
                            )
                        ]
                    )
                )
            ]
        )
                      

def change_page(e) :
    pass








def main(page: Page):
    page.add(
        self_content
        
    )
    page.update()

app(target=main, assets_dir="assets")
