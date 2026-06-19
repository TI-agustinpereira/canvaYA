# codigo playwright

"""
mail: agupereira@tiendainglesa.com.uy
pass: TiendaInglesa123

"""

from playwright.sync_api import sync_playwright
import os

def iniciar_sesion_canva():
    with sync_playwright() as p:
        # Lanza browser con sesion persistente
        context = p.chromium.launch_persistent_context(
            user_data_dir="./canva_session",  # guarda la sesion aca
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        page = context.new_page()
        page.goto("https://www.canva.com")
        
        print("Logueate manualmente en el browser. Cuando termines, presiona Enter aqui...")
        input()
        
        context.storage_state(path="./canva_session/state.json")
        print("Sesion guardada.")
        context.close()

def usar_canva(paths: list[str], diferencias: list[list[int]]):

    paths = [os.path.abspath(ruta) for ruta in paths] # paso de rel path a abs path

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="./canva_session",
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        page = context.new_page()
        page.goto("https://www.canva.com")
        
        
        page.goto("https://www.canva.com/design/DAHMSY2ZMu0/rvHGmWIv0jB3rzj5DE2Ebg/edit")

        # primero edit la slide 5
        page.click("button:has-text('/ 22')")
        page.keyboard.type("5")
        page.keyboard.press("Enter")

        page.wait_for_timeout(200)
        page.dblclick("div#LBXyvYTRMdTfxDRL") # id de tabla en slide 5

        page.click("button:has-text('Import data')")

        with page.expect_file_chooser() as fc_info:
            page.click("button:has-text('Upload data')")
        file_chooser = fc_info.value
        file_chooser.set_files(paths[0])

        page.wait_for_timeout(500)
        page.click("button:has-text('Done')")
        page.wait_for_timeout(1000)

        burbujas_slide_5 = ["LBJXRVpbsMLfd59G", "LBwcGr3TWrpQB7Gq", "LB1zGTCJjMvbDMRs"]

        for i in range(3):

            page.click(f"div#{burbujas_slide_5[i]}")    
            page.wait_for_timeout(100)
            page.keyboard.press("Enter")
            page.wait_for_timeout(100)
            page.keyboard.press("Control+a")
            page.wait_for_timeout(100)
            page.keyboard.press("Backspace")
            page.wait_for_timeout(100)
            page.keyboard.type(f"-{diferencias[0][i]}") if diferencias[0][i] < 0 else page.keyboard.type(f"+{diferencias[0][i]}")

        # segundo edito slide 6
        page.click("button:has-text('/ 22')")   # selector de slide
        page.keyboard.type("6")               # slide de destino
        page.keyboard.press("Enter")

        page.wait_for_timeout(200)
        page.dblclick("div#LBYPZ0QKZzlX64Z0")

        page.click("button:has-text('Import data')")

        with page.expect_file_chooser() as fc_info:
            page.click("button:has-text('Upload data')")
        file_chooser = fc_info.value
        file_chooser.set_files(paths[1])

        page.wait_for_timeout(500)
        page.click("button:has-text('Done')")
        page.wait_for_timeout(1000)

        # slide 7
        page.click("button:has-text('/ 22')")   # selector de slide
        page.keyboard.type("7")               # slide de destino
        page.keyboard.press("Enter")

        page.wait_for_timeout(200)
        page.dblclick("div#LBDxYcR7YV3wyr81")

        page.click("button:has-text('Import data')")

        with page.expect_file_chooser() as fc_info:
            page.click("button:has-text('Upload data')")
        file_chooser = fc_info.value
        file_chooser.set_files(paths[2])

        page.wait_for_timeout(500)
        page.click("button:has-text('Done')")
        page.wait_for_timeout(1000)

        burbujas_slide_7 = ["LBdZn8xjHkS5Lhq5", "LBwjNmc8vwGlTY1h", "LBHZPD0R7wVGwQGD", "LBdJSNWz2jdWHxLS", 
                            "LBjy9mz8V93QnnxY", "LBnCxrgyC40HrXfH", "LB7SDDJ37qqW1qLL", "LBbbP83CM1rPHXMj"]
        
        for i in range(len(burbujas_slide_7)):

            page.click(f"div#{str(burbujas_slide_7[i])}")    
            page.wait_for_timeout(100)
            page.keyboard.press("Enter")
            page.wait_for_timeout(100)
            page.keyboard.press("Control+a")
            page.wait_for_timeout(100)
            page.keyboard.press("Backspace")
            page.wait_for_timeout(100)
            page.keyboard.type(f"{diferencias[1][i]}") if diferencias[1][i] < 0 else page.keyboard.type(f"+{diferencias[1][i]}")
        
        page.wait_for_timeout(800)
        
        context.close()

# primera vez: correr iniciar_sesion_canva()
# las siguientes veces: correr usar_canva() directamente


