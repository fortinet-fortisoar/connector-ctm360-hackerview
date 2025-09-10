## About the connector
HackerView is CTM360’s External Attack Surface Management platform, offering automated asset discovery, issue identification, security ratings, and third-party risk management. This collector lets you pull the issues and assets found on attack surface.
<p>This document provides information about the CTM360 HackerView Connector, which facilitates automated interactions, with a CTM360 HackerView server using FortiSOAR&trade; playbooks. Add the CTM360 HackerView Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with CTM360 HackerView.</p>

### Version information

Connector Version: 1.0.0

Publisher: Fortinet SE

Contributor: Reem Moustafa

Certified: No

## Installing the connector
<p>From FortiSOAR&trade; 6.3.4 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-ctm360-hackerview`

## Prerequisites to configuring the connector
- You must have the URL of CTM360 HackerView server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the CTM360 HackerView server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>CTM360 HackerView</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the Server URL to which you want to connect and perform automated information.<br>
<tr><td>API Key<br></td><td>Specify the API Key to connect to the endpoint and perform automated operations.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 6.3.4 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Issues<br></td><td>Retrieves a list of issues found on your attack surface from CTM360 HackerView based on the filter criteria that you have specified.<br></td><td>get_issues <br/><br></td></tr>
<tr><td>Get Domains<br></td><td>Retrieves a list of your genuine domains from CTM360 HackerView.<br></td><td>get_domains <br/><br></td></tr>
<tr><td>Get Hosts<br></td><td>Retrieves a list of your genuine hostnames from CTM360 HackerView.<br></td><td>get_hosts <br/><br></td></tr>
<tr><td>Get IP Addresses<br></td><td>Retrieves a list of your associated IP addresses from CTM360 HackerView.<br></td><td>get_ip_addresses <br/><br></td></tr>
<tr><td>Get Resolved Issues<br></td><td>Retrieves a list of resolved issues found on your attack surface from CTM360 HackerView based on the filter criteria that you have specified.<br></td><td>get_resolved_issues <br/><br></td></tr>
</tbody></table>

### operation: Get Issues
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>First Seen<br></td><td>Specify the date and time to include only items that appeared for the first time after the given timestamp.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Domains
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get Hosts
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get IP Addresses
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get Resolved Issues
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>From Date<br></td><td>(Optional) Specify the date and time to retrieve results that include only those items that were seen after the specified timestamp.<br>
</td></tr><tr><td>To Date<br></td><td>(Optional) Specify the date and time to retrieve results that include only those items that were seen before the specified timestamp.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - CTM360 HackerView - 1.0.0` playbook collection comes bundled with the CTM360 HackerView connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the CTM360 HackerView connector.

- Get Issues
- Get Domains
- Get Hosts
- Get IP Addresses
- Get Resolved Issues

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
