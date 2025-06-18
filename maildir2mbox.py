#!/usr/bin/env python3

import os
import argparse
import mailbox
from email import policy
from email.parser import BytesParser

def convert_maildir_to_mbox(maildir_path, mbox_path, verbose=False):
    if verbose:
        print(f"🔄 Converting: {maildir_path} → {mbox_path}")
    maildir = mailbox.Maildir(maildir_path, factory=None)
    mbox = mailbox.mbox(mbox_path)

    count = 0
    for key, msg_bytes in maildir.iteritems():
        try:
            parser = BytesParser(policy=policy.default)
            msg = parser.parsebytes(bytes(msg_bytes))
            mbox.add(msg)
            count += 1
        except Exception as e:
            if verbose:
                print(f"⚠️ Error converting message {key}: {e}")
    mbox.flush()
    if verbose:
        print(f"✅ {count} messages exported successfully.")
    return count

def main():
    parser = argparse.ArgumentParser(
        description="Convert Maildir folders (e.g. from Evolution) into MBOX files."
    )
    parser.add_argument(
        "--maildir-root", required=True,
        help="Base directory where Maildir folders are located (e.g. ~/.local/share/evolution/mail/local)"
    )
    parser.add_argument(
        "--prefix", required=True,
        help="Prefix of the folder group to export (e.g. .gmail)"
    )
    parser.add_argument(
        "--output-dir", required=True,
        help="Directory to save the resulting .mbox files"
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    total_exported = 0
    for entry in os.listdir(args.maildir_root):
        if entry.startswith(args.prefix):
            full_path = os.path.join(args.maildir_root, entry)
            if os.path.isdir(full_path) and os.path.isdir(os.path.join(full_path, 'cur')):
                safe_name = entry.replace('.', '_').strip('_')
                out_file = os.path.join(args.output_dir, f"{safe_name}.mbox")
                count = convert_maildir_to_mbox(full_path, out_file, verbose=args.verbose)
                total_exported += count

    print(f"📦 Done. Total messages exported: {total_exported}")

if __name__ == "__main__":
    main()
