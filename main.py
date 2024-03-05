import click

from click import BadParameter

from minikatanacapture import MiniCatanaCapture


@click.command
@click.version_option(version='1.0.1', prog_name='Mini Catana Capture', message=f'{click.style("%(prog)s", fg="bright_magenta")} version {click.style("%(version)s", fg="bright_magenta")}')
@click.option('--video', '-v', help='path of video', required=True)
@click.option('--output', '-o', help='output of image', default='output')
def main(**kwargs):
    """ Mini Catana Capture """
    try:
        app: MiniCatanaCapture = MiniCatanaCapture(**kwargs)
        return app.main()
    except Exception as e:
        raise BadParameter(e)

if(__name__ == '__main__'):
    main()