# ========================================================================
# 🚨 CRITICAL RESOURCE WASTE: VERBOSE DATA STREAMING (DO NOT USE)
# Engineered by: OmniOrigin Group of Businesses
# Description: Demonstrates uncompressed text data wasting cloud tokens.
# ========================================================================
import time

def ship_raw_verbose_payload(sensor_id, temperature, status_message):
    """
    Simulates a basic edge device sending unoptimized, chatty text 
    over an expensive cellular link to a cloud AI endpoint.
    """
    # ❌ CRITICAL TRAP: Heavy, repetitive boilerplate text increases token consumption
    raw_payload = f"System Notification from Gateway Node ID {sensor_id}: The current telemetry scan reports that the temperature is exactly {temperature} degrees Celsius. Additional system diagnostics note: {status_message}."
    
    token_estimate = len(raw_payload.split()) # Rough baseline calculation
    print(f"[*] Shipping Raw Payload ({len(raw_payload)} chars, ~{token_estimate} tokens)...")
    time.sleep(0.5) # Simulating network upload overhead
    
    print("[!] Cloud API billed. Transaction complete.")
    return raw_payload
