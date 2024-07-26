# VPN Split Tunnel
VPN Split Tunnel
This is not the guide how to setup a VPN, but this is a guide how to connect a server/domain/service while connecting a VPN.
This is a solution for you if:
- You're using a VPN that does not allow traffic to one or more particular internet domains
- You need to access those domains while connecting your VPN server.

# How to setup
1. find all related domains of target domain
   1.1 Open new webbrowser tab
   1.2 Open Browser Developer Tools (F12)
   1.3 Access to target domain
   1.4 Go to the 'Network' tab on the Developer tools, and collect the unique domain
2. Configure the domain that you need into the `route_generation.py` file from above domains
   ```
      target_domains = [
      'github.com',
      'api.github.com',
      'avatars.githubusercontent.com',
      'collector.github.com',
      'github.githubassets.com',
      
      # Add further related domain 
      ]
   ```
3. Disconnect the VPN( if connecting)
4. Open terminal and run the command `python /path/to/route_generation.py`
5. Copy the output of the script
6. Execute above command output of the script on your terminal.
# Testing
1. Connect to VPN and try to access to your expected domain.

# Troubleshooting
1. How to reset routing table on your local machine
   - Run command `sudo route -n flush`
   - Turn off and on your wifi on your local machine (MacOS command line: `sudo ifconfig en0 <down|up>`)
2. The local machine unable connect to expected domain while using VPN.
   - Try to reset your routing table and redo the setup steps.
   - You may need to disconnect the VPN before run the `route_generation.py` file
   - 
