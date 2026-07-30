outage_records = [
    {"region": "North Zone", "duration": 4.5, "consumers_affected": 6200},
    {"region": "South Hub", "duration": 1.5, "consumers_affected": 1200},
    {"region": "East Coast", "duration": 6.0, "consumers_affected": 4500},
    {"region": "West Metro", "duration": 3.0, "consumers_affected": 8900},
    {"region": "Central Grid", "duration": 2.2, "consumers_affected": 3100}
]

def analyze_outages(records):
    print("--- POWER OUTAGE ANALYSIS ---")
    
    if not records:
        print("No outage records found.")
        return

    total_duration = 0.0
    longest_duration = -1.0
    longest_region = ""
    regions_above_5k = []

    for record in records:
        duration = record["duration"]
        consumers = record["consumers_affected"]
        region = record["region"]
        total_duration += duration
        
        if duration > longest_duration:
            longest_duration = duration
            longest_region = region
            
        if consumers > 5000:
            regions_above_5k.append(record)

    print(f"\n1. Region with Longest Outage:\n   {longest_region} ({longest_duration} hours)")


    print(f"\n2. Total Outage Duration across all regions:\n   {total_duration:.2f} hours")


    print("\n3. Regions Affecting More Than 5,000 Consumers:")
    if regions_above_5k:
        for r in regions_above_5k:
            print(f"   - {r['region']}: {r['consumers_affected']:,} consumers affected")
    else:
        print("   None")

    avg_duration = total_duration / len(records)
    print(f"\n4. Average Outage Duration:\n   {avg_duration:.2f} hours")

    print("\n5. Regions Sorted by Outage Duration (Shortest to Longest):")
    sorted_records = sorted(records, key=lambda x: x["duration"])
    for sr in sorted_records:
        print(f"   {sr['duration']} hours -> {sr['region']}")

if __name__ == "__main__":
    analyze_outages(outage_records)
