#!/usr/bin/env python3
"""
Test script to show the exact prompt that gets sent to the LLM.
"""

import sys
import os
from datetime import datetime

# Add the src directory to the path so we can import cmdrx modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cmdrx.core import CmdRxCore

def test_prompt_generation():
    """Generate and display a sample prompt."""
    
    # Create a test context similar to what would be generated
    test_context = {
        'command': 'systemctl status apache2',
        'output': '''● apache2.service - The Apache HTTP Server
   Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
   Active: failed (Result: exit-code) since Mon 2024-12-01 15:30:45 UTC; 5min ago
  Process: 1234 ExecStart=/usr/sbin/apache2ctl start (code=exited, status=1/FAILURE)
    Tasks: 0 (limit: 4915)
   Memory: 0B
   CGroup: /system.slice/apache2.service

Dec 01 15:30:45 server systemd[1]: Starting The Apache HTTP Server...
Dec 01 15:30:45 server apache2[1234]: AH00526: Syntax error on line 25 of /etc/apache2/sites-enabled/000-default.conf:
Dec 01 15:30:45 server apache2[1234]: Invalid command 'DocumentRoo', perhaps misspelled or defined by a module not included in the server configuration
Dec 01 15:30:45 server systemd[1]: apache2.service: Control process exited, code=exited, status=1/FAILURE
Dec 01 15:30:45 server systemd[1]: apache2.service: Failed with result 'exit-code'.
Dec 01 15:30:45 server systemd[1]: Failed to start The Apache HTTP Server.''',
        'return_code': 3,
        'timestamp': datetime.now().isoformat(),
        'system_info': {
            'os': 'Linux',
            'os_version': '5.15.0',
            'architecture': 'x86_64',
            'hostname': 'test-server',
            'user': 'admin'
        }
    }
    
    # Create a mock core instance (we don't need full initialization for this test)
    class MockCore:
        def _generate_prompt(self, context):
            prompt_parts = [
                "You are CmdRx, an expert system administrator AI assistant specialized in Linux/Unix systems.",
                "Analyze the following command output and provide detailed troubleshooting information.",
                "",
                f"Command executed: {context['command']}",
            ]
            
            if context['return_code'] is not None:
                status_desc = "SUCCESS" if context['return_code'] == 0 else "FAILURE"
                prompt_parts.append(f"Exit code: {context['return_code']} ({status_desc})")
            
            # Add system context if available
            system_info = context.get('system_info', {})
            if system_info:
                prompt_parts.extend([
                    "",
                    "System context:",
                    f"- OS: {system_info.get('os', 'Unknown')} {system_info.get('os_version', '')}",
                    f"- Architecture: {system_info.get('architecture', 'Unknown')}",
                    f"- User: {system_info.get('user', 'Unknown')}",
                ])
            
            prompt_parts.extend([
                "",
                "Command output:",
                "```",
                context['output'],
                "```",
                "",
                "Please provide your analysis in the following JSON format:",
                "{",
                '  "analysis": "Comprehensive analysis of what the output shows and what it means",',
                '  "status": "success|warning|error|info",',
                '  "issues": ["specific", "issues", "identified", "from", "output"],',
                '  "troubleshooting_steps": [',
                '    {',
                '      "step": 1,',
                '      "description": "Clear step description",',
                '      "command": "exact command to run (if applicable)",',
                '      "explanation": "Why this step helps diagnose or resolve the issue"',
                '    }',
                '  ],',
                '  "suggested_fixes": [',
                '    {',
                '      "description": "What this fix accomplishes",',
                '      "commands": ["command1", "command2"],',
                '      "risk_level": "low|medium|high",',
                '      "explanation": "Detailed explanation of the fix and potential impact"',
                '    }',
                '  ],',
                '  "additional_info": "Relevant background information, best practices, or warnings"',
                "}",
                "",
                "Analysis guidelines:",
                "- Provide specific, actionable troubleshooting steps",
                "- Include exact commands when helpful (with proper syntax)",
                "- Clearly categorize risk levels: LOW (safe), MEDIUM (requires caution), HIGH (potential data loss)",
                "- Focus on the most probable root causes based on the error patterns",
                "- Consider common system administration scenarios and solutions",
                "- If successful output, highlight what's working well and any optimization opportunities",
                "- For errors, provide both immediate fixes and preventive measures",
                "- Include relevant log file locations or configuration files to check",
            ])
            
            return "\n".join(prompt_parts)
    
    mock_core = MockCore()
    prompt = mock_core._generate_prompt(test_context)
    
    print("=" * 80)
    print("FULL PROMPT SENT TO LLM")
    print("=" * 80)
    print("\n🎭 SYSTEM MESSAGE:")
    print("You are CmdRx, an expert system administrator AI assistant. Provide detailed, accurate troubleshooting information.")
    print("\n📝 USER PROMPT:")
    print("-" * 40)
    print(prompt)
    print("-" * 40)
    print(f"\n📊 PROMPT STATISTICS:")
    print(f"Total characters: {len(prompt)}")
    print(f"Total lines: {len(prompt.split(chr(10)))}")
    print(f"Temperature: 0.1 (low for consistent responses)")

if __name__ == "__main__":
    test_prompt_generation()