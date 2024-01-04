#!/bin/bash

# Function to get the current date in YYYY-MM-DD format
get_current_date() {
  date +"%Y-%m-%d"
}

# Function to create a new Markdown file with YAML front matter
create_markdown_file() {
  local path=$1
  local filename=$2
  local date=$(get_current_date)

  # Create the file with the specified path and filename
  fullpath="${path}/${filename}.md"

  touch $fullpath

  # Add YAML front matter to the file
  echo "---" >> "${fullpath}"
  echo "date: ${date}" >> "${fullpath}"
  echo "---" >> "${fullpath}"
  echo "" >> "${fullpath}"
  echo "#" >> "${fullpath}"

  echo "Created ${fullpath} with YAML front matter."

  # open new file in vscode in current directory
  code $fullpath .
}

# Usage: new-til.sh <path> <filename>
if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <path> <filename>"
  exit 1
fi

path=$1
filename=$2

# Check if the specified path exists
if [[ ! -d "$path" ]]; then
  # Create the path if it doesn't exist
  mkdir -p "$path"
fi

# Check if the path creation was successful
if [[ ! -d "$path" ]]; then
  echo "Failed to create the path: $path"
  exit 1
fi

create_markdown_file "$path" "$filename"
