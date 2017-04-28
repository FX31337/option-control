import optparse
import os
import sys

def parseOpts():
    parser = optparse.OptionParser()
    parser.add_option('-v', '--verbose', dest='verbose', action='store_true',
        help='Increase output verbosity.')
    parser.add_option('-c', '--config-path', dest='config_path', metavar='PATH',
        help='Location of the configuration file.')
    parser.add_option('-n', '--netrc', dest='usenetrc', action='store_true', default=False,
        help='User .netrc authentication data.')
    parser.add_option('-U', '--user-agent', dest='user_agent', metavar='UA',
        help='Specify a custom user agent.')
    parser.add_option('--referer', dest='referer', default=None,
        help='Specify a custom referer, if access is restricted to one domain.')
    parser.add_option('-R', '--retries', dest='retries', metavar='RETRIES', default=10,
        help='Number of retries (default is %default).')
    parser.add_option('-H', '--add-header', dest='headers', action='append',
        help='Specify a custom HTTP header and its value separated by a colon \':\'.')
    parser.add_option('-p', '--provider', dest='provider', metavar='PROVIDER',
        help='Select a provider (e.g. 365binaryoption).')

    opts, args = parser.parse_args()
    if opts.config_path:
        if os.path.isdir(args.config_path):
            args.config_path = os.path.join(args.config_path, 'option_control.conf')
        if not os.path.exists(args.config_path):
            parser.error('Config does not exist at %s.' % args.config_path)

    if opts.verbose:
        for label, conf in (
            ('Command-line args', sys.argv[1:]),
        ):
            print('[debug] %s: %s' % (label, conf))
    return parser, opts, args
