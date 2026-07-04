#!/usr/bin/env python3

# Amazon Login OTP Page

def print_otp_login_page():
    """Display the OTP login page"""
    page = """
    ╔════════════════════════════════════════════╗
    ║         AMAZON LOGIN - OTP VERIFICATION    ║
    ╚════════════════════════════════════════════╝
    
    Please enter the One-Time Password (OTP) sent to your registered email/phone.
    
    ┌────────────────────────────────────────────┐
    │ Email/Phone: *****@example.com             │
    │                                            │
    │ Enter OTP: [________________]              │
    │                                            │
    │ [  VERIFY  ]        [  RESEND OTP  ]      │
    │                                            │
    │ ☐ Trust this device for 30 days           │
    │                                            │
    │ Didn't receive the code? Check spam        │
    │ folder or request a new code.              │
    │                                            │
    │ [ Back to Login ]                         │
    └────────────────────────────────────────────┘
    
    Security Note: Never share your OTP with anyone.
    Amazon will never ask for your OTP via email or phone.
    """
    print(page)

if __name__ == "__main__":
    print_otp_login_page()
