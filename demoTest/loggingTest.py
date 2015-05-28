import logging
logger = logging.getLogger( 'loggingTtt' )
# logging.basicConfig(filename="logs/log.txt", level=logging.DEBUG)
def some_method():
    logger.debug('begin of some_method')
def main():
 
    # Produce formater first
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
 
    # Setup Handler
    # console = logging.StreamHandler()
    # console.setLevel(logging.DEBUG)
    # console.setFormatter(formatter)
    
    fileHandler = logging.FileHandler("logs/log.txt")
    fileHandler.setFormatter(formatter)

    # Setup Logger
    # logger.addHandler(console)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)

    some_method()
 
if __name__ == '__main__':
    main()

    # logger = logging.getLogger( __name__ )
    # logger.debug("XXX")