#!/usr/bin/env python3
"""
Tests for document processor
"""

import unittest
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.document_processor import DocumentProcessor


class TestDocumentProcessor(unittest.TestCase):
    
    def setUp(self):
        self.processor = DocumentProcessor()
    
    def test_text_document_processing(self):
        """Test processing of plain text documents"""
        content = b"Hello, this is a test document."
        result = self.processor.process_document(content, 'txt')
        self.assertEqual(result, "Hello, this is a test document.")
    
    def test_html_document_processing(self):
        """Test processing of HTML documents"""
        content = b"<html><body><h1>Title</h1><p>Content</p></body></html>"
        result = self.processor.process_document(content, 'html')
        self.assertIn("Title", result)
        self.assertIn("Content", result)
    
    def test_unsupported_file_type(self):
        """Test handling of unsupported file types"""
        content = b"Some content"
        result = self.processor.process_document(content, 'unknown')
        self.assertEqual(result, "")
    
    def test_rtf_document_processing(self):
        """Test basic RTF processing"""
        content = b"{\\rtf1 Hello \\b World}"
        result = self.processor.process_document(content, 'rtf')
        self.assertIn("Hello", result)
        self.assertIn("World", result)


if __name__ == '__main__':
    unittest.main()