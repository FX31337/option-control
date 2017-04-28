#!/usr/bin/env python3
# Usage:
# - python3 option_control/__main__.py --help
# - python3 -m option_control --help

from .options import parseOpts

def _main():

    # Parse options from the command-line.
    parser, opts, args = parseOpts()

    # Set user agent.
    if opts.user_agent is not None:
        headers['User-Agent'] = opts.user_agent

    # Set referer.
    if opts.referer is not None:
        headers['Referer'] = opts.referer

    # Custom HTTP headers.
    if opts.headers is not None:
        for h in opts.headers:
            if ':' not in h:
                parser.error('\nERROR: Wrong header formatting, it should be key:value, not "%s"' % h)
            key, value = h.split(':', 1)
            if opts.verbose:
                print('[debug] Adding header: %s:%s\n' % (key, value))
            headers[key] = value

def main():
    try:
        _main()
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')
