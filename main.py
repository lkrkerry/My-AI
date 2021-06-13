import functions
# from modules import myNL

if __name__ == "__main__":
    Kristina = functions.robots.AI()
    try:
        Kristina.start()
    except Exception as e:
        functions.log_in(e,level="error")