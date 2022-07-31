import logging

logging.basicConfig( level=logging.INFO, format='%(asctime)s [%(levelname)s][%(process)d][%(thread)d] %(pathname)s %(funcName)s %(lineno)d: %(message)s' )
logger=logging.getLogger( "log_demo" )
def aa():
    logger.info( 'info' )
    logger.debug( 'debug' )
    logger.warning( 'warning' )
aa()