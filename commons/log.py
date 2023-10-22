import logging

from .configs import Config

logging.basicConfig(format='%(levelname)s\t%(message)s',
                    level=Config.log_level)
Logger = logging.getLogger(__name__)
