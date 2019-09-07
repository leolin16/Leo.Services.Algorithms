# Spunk

## Five Pillars of Splunk Knowledge

1. Data Interpretation
   > Fields and field extractions(key=value pair)
   > 1. ip_address=68.147.170.101 (easy to detect)
   > 2. ip_address 10.50.161.3 (easy to detect)
   > 3. 9:20 404 stevej 10.10.1.5
2. Data Classification(Event Types & Transactions)
   > Event properties:
   > 1. Timestamp
   > 2. Host
   > 3. Source
   > 4. Source type

    eg: an event from apache log:
    > 172.26.34.223--[01/Jul/2017:12:05:27 -0700] "GET /trade/app?action=logout HTTP/1.1" 200 2953

    Timestamp: [01/Jul/2017:12:05:27 -0700]
    Host: 172.26.34.223
    Source: "GET /trade/app?action=logout HTTP/1.1" 200 2953

    Event types(same search string):
    eventtype=valid/invalid
   > stats count by eventtype

   returns: valid - 2, invalid - 3

   Transaction(a series of events): trace a full trade
3. Data Enrichment(Loopups and workflow actions)
   1. CSV
   2. External
   3. Geo
   4. KV Store

   eg: regions.csv with regioncode like a1bf2g58 and regionname like US East
   > lookup regions.csv regioncode OUTPUT regionname
4. Data Normalization(Tags & Aliases)
   Tags: eg: Tag=webservers
   Aliases: normalize data from multiple sources, one field to many alias
   > rename \<oldfieldname> as \<newfieldname>

   another example:
   > eval \<newfieldname>=coalesce(\<oldfieldname1>, \<oldfieldname2>)
5. Data Models(hierarchy of data sets)
   Datamodel -> Dataset1(Events) + Dataset2(Searches) + Dataset3(Transactions)
   Data sets are hierarchy of knowledge objects

## Usage Scenarios

1. System Admin
2. Visualization tools(build tables and excel skills)
3. Data Nerd
4. Analyst
5. Architect
6. Security

## Machine Data

1. Operational Intelligence
2. IOT
3. Mobile Devices
4. Web Service Requests
5. Apache log files
6. Security logs

characteristics:

1. semi structured
2. machine-generated
3. often overlooked

source types:

1. Servers
2. Cloud
3. Workstations
4. Regex(logs)

sources:

1. Local Machine
2. Forwarders
3. Upload Sources (csv, tsv, apache logs, etc.)
4. Example Data

## Splunk Architecture

1. Search Head(write queries, create msg alerts)
2. Index(say hot/cold, more than one splunk instances)
3. Forwarder(agents run on devices to send data to splunk)

## price and license by Ingest

1. Splunk Free
   > 500MB/Day
2. Splunk Enterprise
3. > Varies(Term vs. Perpetual)
4. Splunk Cloud

## Installation

### Windows

1. install from msi on win 10/server 64bit
2. setup splunk env account(different from online account)
3. access localhost:8000

### Mac OS

1. install from tgz or dmg

### Linux

1. rpm for red hat/cent os
    > yum install wget \
    > yum install net-tools \

    ***set current mode from enforcing to permissive***
    > sestatus \
    > setenforce 0 \
    > wget ???.rpm \
    > chmod 744 ???.rpm \
    > rpm -i ???.rpm \

    ***Start up Splunk***
    > /opt/splunk/bin/splunk start --accept-license
2. deb for ubuntu/debian