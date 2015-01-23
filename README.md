# Google Group Settings Audit

This is a script to help audit the settings of groups on a google apps domain

### Steps to Use

 1. setup a google api project https://console.developers.google.com/
 2. enable the following apis: "Groups Settings API" and "Admin SDK"
 3. setup the Oauth2 Callback as `http://localhost:8080/`
 4. `pip install python-gflags oauth2client tornado`
 5. run `python audit_groups.py --client-id=... --client-secret=... --domain=yourdomain.com`

Expected Output:

```xml
team@yourcompany.com
<?xml version="1.0" encoding="UTF-8"?>
<entry xmlns="http://www.w3.org/2005/Atom" xmlns:apps="http://schemas.google.com/apps/2006" xmlns:gd="http://schemas.google.com/g/2005">
 <id>tag:googleapis.com,2010:apps:groupssettings:GROUP:team@yourcompany.com</id>
 <title>Groups Resource Entry</title>
 <content type="text">admin</content>
 <author>
  <name>Google</name>
 </author>
 <apps:email>team@yourcompany.com</apps:email>
 <apps:name>team</apps:name>
 <apps:description/>
 <apps:whoCanJoin>CAN_REQUEST_TO_JOIN</apps:whoCanJoin>
 <apps:whoCanViewMembership>ALL_IN_DOMAIN_CAN_VIEW</apps:whoCanViewMembership>
 <apps:whoCanViewGroup>ALL_IN_DOMAIN_CAN_VIEW</apps:whoCanViewGroup>
 <apps:whoCanInvite>ALL_MANAGERS_CAN_INVITE</apps:whoCanInvite>
 <apps:allowExternalMembers>false</apps:allowExternalMembers>
 <apps:whoCanPostMessage>ANYONE_CAN_POST</apps:whoCanPostMessage>
 <apps:allowWebPosting>true</apps:allowWebPosting>
 <apps:maxMessageBytes>5242880</apps:maxMessageBytes>
 <apps:isArchived>true</apps:isArchived>
 <apps:archiveOnly>false</apps:archiveOnly>
 <apps:messageModerationLevel>MODERATE_NONE</apps:messageModerationLevel>
 <apps:spamModerationLevel>ALLOW</apps:spamModerationLevel>
 <apps:replyTo>REPLY_TO_IGNORE</apps:replyTo>
 <apps:customReplyTo/>
 <apps:sendMessageDenyNotification>false</apps:sendMessageDenyNotification>
 <apps:defaultMessageDenyNotificationText/>
 <apps:showInGroupDirectory>false</apps:showInGroupDirectory>
 <apps:allowGoogleCommunication>false</apps:allowGoogleCommunication>
 <apps:membersCanPostAsTheGroup>false</apps:membersCanPostAsTheGroup>
 <apps:messageDisplayFont>DEFAULT_FONT</apps:messageDisplayFont>
 <apps:includeInGlobalAddressList>true</apps:includeInGlobalAddressList>
 <apps:whoCanLeaveGroup>ALL_MEMBERS_CAN_LEAVE</apps:whoCanLeaveGroup>
 <apps:whoCanContactOwner>ANYONE_CAN_CONTACT</apps:whoCanContactOwner>
</entry>
****************************************
...[repeating for each group]
```