class Error(Exception):
    """Base class for other exceptions"""
    pass


class Summoner_Name_Not_Valid(Error):
    """Raised when the Username input is not a real Username"""
    pass


class Api_not_valid(Error):
    """Raised when the Api input is not valid"""
    pass

