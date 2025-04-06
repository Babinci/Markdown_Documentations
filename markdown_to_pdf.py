#!/usr/bin/env python
import os
import sys
import io
import argparse
from markdown_it import MarkdownIt
from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import HtmlFormatter
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, HRFlowable, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
import re
import html

# Define custom page size for 10-inch e-reader (approximate dimensions)
# Most 10-inch e-readers are around 7.8 x 5.8 inches for reading area
EREADER_WIDTH = 6 * inch
EREADER_HEIGHT = 8 * inch
EREADER_PAGESIZE = (EREADER_WIDTH, EREADER_HEIGHT)

def markdown_to_pdf(markdown_path, output_path=None):
    """Convert markdown file to PDF."""
    if not os.path.exists(markdown_path):
        print(f"Error: File not found - {markdown_path}")
        return False
    
    # If output path is not specified, use the markdown filename with .pdf extension
    if not output_path:
        output_path = os.path.splitext(markdown_path)[0] + '.pdf'
    
    # Read markdown content
    with open(markdown_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Setup markdown parser with syntax highlighting for code blocks
    def highlight_code(code, lang, attrs):
        if not lang:
            return f'<pre class="no-language"><code>{html.escape(code)}</code></pre>'
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = HtmlFormatter(style='default', linenos=False, cssclass='codehilite')
            result = highlight(code, lexer, formatter)
            return f'<div class="code-block">{result}</div>'
        except Exception:
            return f'<pre class="language-{lang}"><code>{html.escape(code)}</code></pre>'
    
    # Initialize markdown-it with code highlighting
    md = MarkdownIt('commonmark', {'highlight': highlight_code})
    html_content = md.render(md_content)
    
    # Create PDF with the HTML content
    create_pdf(html_content, output_path)
    return True

def create_pdf(html_content, output_path):
    """Create PDF from HTML content using ReportLab."""
    # Create PDF document for e-reader
    doc = SimpleDocTemplate(
        output_path,
        pagesize=EREADER_PAGESIZE,
        leftMargin=0.5*inch,
        rightMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Add custom styles
    styles.add(ParagraphStyle(
        name='CustomCodeBlock',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=8,
        leading=10,
        leftIndent=20,
        rightIndent=20,
        backColor=colors.lightgrey,
        borderWidth=1,
        borderColor=colors.grey,
        borderPadding=5,
        spaceAfter=10,
        spaceBefore=10
    ))
    
    styles.add(ParagraphStyle(
        name='CustomHeading1',
        parent=styles['Heading1'],
        textColor=colors.black,
        fontSize=16,
        leading=20,
        spaceAfter=12
    ))
    
    styles.add(ParagraphStyle(
        name='CustomHeading2',
        parent=styles['Heading2'],
        textColor=colors.black,
        fontSize=14,
        leading=18,
        spaceAfter=10
    ))
    
    styles.add(ParagraphStyle(
        name='CustomHeading3',
        parent=styles['Heading3'],
        textColor=colors.black,
        fontSize=12,
        leading=16,
        spaceAfter=8
    ))
    
    styles.add(ParagraphStyle(
        name='CustomHeading4',
        parent=styles['Heading4'],
        textColor=colors.black,
        fontSize=10,
        leading=14,
        spaceAfter=6
    ))
    
    styles.add(ParagraphStyle(
        name='CustomBlockquote',
        parent=styles['Normal'],
        leftIndent=30,
        rightIndent=30,
        fontStyle='Italic',
        spaceAfter=12,
        spaceBefore=12,
        borderWidth=1,
        borderColor=colors.lightgrey,
        borderPadding=8,
        borderRadius=5
    ))
    
    styles.add(ParagraphStyle(
        name='CustomParagraph',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        spaceAfter=10
    ))
    
    # Create a list to hold the elements of the PDF
    elements = []
    
    # Process the HTML content
    lines = html_content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Code blocks - look for either <pre> or <div class="code-block">
        if line.startswith('<pre') or line.startswith('<div class="code-block">'):
            code_content = []
            in_code_block = True
            
            # If it's a div.code-block, we need to extract from the inner pre
            if line.startswith('<div class="code-block">'):
                # Find the pre inside
                start_idx = i
                while i < len(lines) and '</div>' not in lines[i]:
                    if '<pre' in lines[i]:
                        i += 1  # Skip the pre tag
                        while i < len(lines) and '</pre>' not in lines[i]:
                            code_content.append(lines[i])
                            i += 1
                    i += 1
                # Clean up code block content
                code_text = '\n'.join(code_content)
                code_text = re.sub('<.*?>', '', code_text)  # Remove HTML tags
                code_text = html.unescape(code_text)        # Unescape HTML entities
                elements.append(Preformatted(code_text, styles['CustomCodeBlock']))
                elements.append(Spacer(1, 12))
            else:  # It's a regular <pre> tag
                i += 1  # Skip the opening pre tag
                while i < len(lines) and '</pre>' not in lines[i]:
                    code_content.append(lines[i])
                    i += 1
                # Clean up code block content
                code_text = '\n'.join(code_content)
                code_text = re.sub('<.*?>', '', code_text)  # Remove HTML tags
                code_text = html.unescape(code_text)        # Unescape HTML entities
                elements.append(Preformatted(code_text, styles['CustomCodeBlock']))
                elements.append(Spacer(1, 12))
            
            i += 1  # Move past the closing tag
            continue
        
        # Headings
        elif line.startswith('<h1>'):
            text = re.sub('<.*?>', '', line)
            elements.append(Paragraph(text, styles['CustomHeading1']))
            elements.append(Spacer(1, 12))
        elif line.startswith('<h2>'):
            text = re.sub('<.*?>', '', line)
            elements.append(Paragraph(text, styles['CustomHeading2']))
            elements.append(Spacer(1, 10))
        elif line.startswith('<h3>'):
            text = re.sub('<.*?>', '', line)
            elements.append(Paragraph(text, styles['CustomHeading3']))
            elements.append(Spacer(1, 8))
        elif line.startswith('<h4>'):
            text = re.sub('<.*?>', '', line)
            elements.append(Paragraph(text, styles['CustomHeading4']))
            elements.append(Spacer(1, 6))
        
        # Blockquotes
        elif line.startswith('<blockquote>'):
            quote_content = []
            i += 1
            while i < len(lines) and not lines[i].strip().endswith('</blockquote>'):
                quote_content.append(lines[i])
                i += 1
            
            if i < len(lines):
                quote_content.append(lines[i])
            
            # Extract text from blockquote
            quote_text = ' '.join(quote_content)
            quote_text = re.sub('<.*?>', '', quote_text)
            quote_text = html.unescape(quote_text)
            
            elements.append(Paragraph(quote_text, styles['CustomBlockquote']))
            elements.append(Spacer(1, 12))
        
        # Paragraphs
        elif line.startswith('<p>'):
            text = re.sub('<.*?>', '', line)
            text = html.unescape(text)
            # Convert markdown bold/italic to ReportLab tags
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
            
            elements.append(Paragraph(text, styles['CustomParagraph']))
            elements.append(Spacer(1, 10))
        
        # Horizontal rules
        elif line.startswith('<hr'):
            elements.append(HRFlowable(width="100%", thickness=1, color=colors.black))
            elements.append(Spacer(1, 12))
        
        # Skip empty lines
        elif not line:
            pass
        
        # Other HTML - try to extract text
        else:
            text = re.sub('<.*?>', '', line)
            text = html.unescape(text)
            if text.strip():
                elements.append(Paragraph(text, styles['CustomParagraph']))
                elements.append(Spacer(1, 8))
        
        i += 1
    
    # Build the PDF document
    doc.build(elements)
    print(f"PDF successfully created: {output_path}")
    return True

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(
        description='Convert Markdown files to PDF with black and white formatting optimized for e-readers',
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Add arguments
    parser.add_argument(
        'input_file', 
        nargs='?', 
        default="supabase/actual.md",
        help='Path to the input markdown file'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Path to the output PDF file (defaults to the same name as input with .pdf extension)'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Convert markdown to PDF
    markdown_to_pdf(args.input_file, args.output)

if __name__ == "__main__":
    main()
