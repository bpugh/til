"Run this after build_database.py - it needs til.db"
import pathlib
import sqlite_utils
import sys
import re

root = pathlib.Path(__file__).parent.resolve()

index_re = re.compile(r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL)

if __name__ == "__main__":
    db = sqlite_utils.Database(root / "til.db")
    by_topic = {}
    for row in db["til"].rows_where(order_by="created_utc"):
        by_topic.setdefault(row["topic"], []).append(row)

    # Sort the topics alphabetically
    sorted_topics = sorted(by_topic.keys())

    index = ["<!-- index starts -->"]
    index.append(f'{db["til"].count} TILs and counting...\n')

    # Loop over the sorted topic list
    for topic in sorted_topics:
        rows = by_topic[topic]
        index.append("## {}\n".format(topic))
        for row in rows:
            index.append("* [{title}]({url}) - {date}".format(**row))
        index.append("")

    if index[-1] == "":
        index.pop()
    index.append("<!-- index ends -->")

    if "--rewrite" in sys.argv:
        readme = root / "README.md"
        index_txt = "\n".join(index).strip()
        readme_contents = readme.open().read()
        readme.open("w").write(index_re.sub(index_txt, readme_contents))
    else:
        print("\n".join(index))
