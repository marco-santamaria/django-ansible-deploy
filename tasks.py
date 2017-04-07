from invoke import task
from pycon8 import __version__
from pkg_resources import parse_version


@task
def clean(ctx, cache=False, build=False, dist=False, docs=False, wipe=False):
    if cache or wipe:
        ctx.run('find . -type d -name "__pycache__" -exec rm -fr {} +')
    if build or wipe:
        ctx.run('rm -rf build/*')
    if dist or wipe:
        ctx.run('rm -rf dist/*')
    if docs or wipe:
        ctx.run('rm -rf docs/build/*')


@task
def build(ctx, bundle=False, docs=False):
    if bundle:
        version = str(parse_version(__version__))
        ctx.run('pip wheel -r requirements/prod.txt --wheel-dir=deploy/files/tmp')
        ctx.run(
            'cd deploy/files/tmp && tar -cjvf ../pycon8-{}-bundle.tar.bz2 *'
            .format(version))
        ctx.run('rm -rf deploy/files/tmp')
