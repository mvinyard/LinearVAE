
import licorice_font


def _no_transform(x):
    return x

def _print_model(encoder, decoder):

    try:
        licorice_font.underline("Encoder:", n_newline=0)
        print(encoder)
        licorice_font.underline("\nDecoder:", n_newline=0)
        print(decoder)
    except:
        print(encoder)
        print(decoder)