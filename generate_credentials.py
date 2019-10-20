# -*- coding: utf-8 -*- #

"""
"""

import pickle as pkl
import argparse


def main(id, password, event_name, ifttt_token):
    with open("credential.pkl", 'wb+') as f:
        pkl.dump({"id": id, "password": password, "event_name": event_name, "ifttt_token": ifttt_token}, f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate credential pickle file")
    parser.add_argument('--id', type=str, required=True,
                        help="Your Seikyou ID")
    parser.add_argument('--password', type=str, required=True,
                        help="Your Seikyou password")
    parser.add_argument('--event_name', type=str, required=True,
                        help="IFTTT webhook event name")
    parser.add_argument('--ifttt_token', type=str, required=True,
                        help="IFTTT webhook token")
    args = parser.parse_args()
    main(args.id, args.password, args.event_name, args.ifttt_token)
