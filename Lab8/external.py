#!/usr/bin/env python
# coding: utf8

import socket

MAX_PACKET = 32768

def recv_all(sock):

    prev_timeout = sock.gettimeout()
    try:
        sock.settimeout(0.01)

        rdata = []
        while True:
            try:
                rdata.append(sock.recv())
            except socket.timeout:
                return ''.join(rdata)

        # unreachable
    finally:
        sock.settimeout(prev_timeout)

def normalize_line_endings(s):
    r'''Convert string containing various line endings like \n, \r or \r\n,
    to uniform \n.'''

    return ''.join((line + '\n') for line in s.splitlines())

def run():
    r'''Main loop'''


    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, \
                                socket.IPPROTO_TCP)
    server_sock.bind(('', 5555))
    server_sock.listen(1)

    while True:
        # accept connection
        client_sock, client_addr = server_sock.accept()


        request = normalize_line_endings(recv_all(client_sock)) # hack again
        request_head, request_body = request.split('\n\n', 1)


        request_head = request_head.splitlines()
        request_headline = request_head[0]

        request_headers = dict(x.split(': ', 1) for x in request_head[1:])


        request_method, request_uri, request_proto = request_headline.split(' ', 3)

        response_body = [
            '<html><body><h1>Hello, world!</h1>',
            '<p>This page is in location %(request_uri)r, was requested ' % locals(),
            'using %(request_method)r, and with %(request_proto)r.</p>' % locals(),
            '<p>Request body is %(request_body)r</p>' % locals(),
            '<p>Actual set of headers received:</p>',
            '<ul>',
        ]

        for request_header_name, request_header_value in request_headers.iteritems():
            response_body.append('<li><b>%r</b> == %r</li>' % (request_header_name, \
                                                    request_header_value))

        response_body.append('</ul></body></html>')

        response_body_raw = ''.join(response_body)


        response_headers = {
            'Content-Type': 'text/html; encoding=utf8',
            'Content-Length': len(response_body_raw),
            'Connection': 'close',
        }

        response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in \
                                                response_headers.iteritems())


        response_proto = 'HTTP/1.1'
        response_status = '200'
        response_status_text = 'OK' # this can be random


        client_sock.send('%s %s %s' % (response_proto, response_status, \
                                                        response_status_text))
        client_sock.send(response_headers_raw)
        client_sock.send('\n')
        client_sock.send(response_body_raw)


        client_sock.close()

run()