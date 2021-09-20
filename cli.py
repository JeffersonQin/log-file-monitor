import click
import time


@click.group()
def cli():
	pass


@cli.command()
@click.option('--interval', default=1000, help='interval of refreshing (milliseconds)')
@click.option('--show_length', default=True, type=click.BOOL, help='whether show file length')
@click.option('--show_line', default=True, type=click.BOOL, help='whether show file line count')
@click.argument('file')
def monitor(interval, show_length, show_line, file):
	'''
	monitor file status
	'''
	while True:
		with open(file, 'r', encoding='utf8') as f:
			content = str(f.read())
			length = len(content)
			line = content.count('\n')
			print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), file)
			if (show_length):
				print('file length:', length)
			if (show_line):
				print('line count:', line)
			time.sleep(interval / 1000)


if __name__ == '__main__':
	cli()
