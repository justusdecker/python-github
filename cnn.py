def cret(text: str, color: tuple[int,int,int]) -> str:
    """ Uses Escape Seqs to colorize a string. """
    color = hex_to_rgb(color)
    return f"\033[38;2;{color[0]};{color[1]};{color[2]}m{text}\033[39m"

def hex_to_rgb(text: str) -> tuple[int,int,int]:
    """ converts a string(Must be a hex value! Otherwise it will raise an Exception!) """
    
    return int(text[1:3],16),int(text[3:5],16),int(text[5:7],16)