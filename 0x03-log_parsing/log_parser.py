#!/usr/bin/python3

import sys

def compute_metrics(lines):
    total_lines = len(lines)
    total_chars = sum(len(line) for line in lines)
    average_length = total_chars / total_lines if total_lines > 0 else 0

    return {
        'total_lines': total_lines,
        'total_chars': total_chars,
        'average_length': average_length
    }

def main():
    input_lines = []
    
    print("Enter lines of text (Ctrl+D or Ctrl+Z to finish):")
    
    try:
        while True:
            line = input()
            input_lines.append(line)
    except KeyboardInterrupt:
        pass
    
    metrics = compute_metrics(input_lines)

    print("Metrics:")
    print("Total lines:", metrics['total_lines'])
    print("Total characters:", metrics['total_chars'])
    print("Average line length:", metrics['average_length'])

if __name__ == "__main__":
    main()
