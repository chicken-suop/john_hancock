# John Hancock
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/john_hancock/?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

The best amalgamation of eSigning software, EVER!

## Installation

#### 1. Install Pre-requisites

	pip install signaturit_sdk

#### 2. Install John Hancock

	bench get-app john_hancock https://github.com/ratskin/john_hancock.git
	bench install-app john_hancock

#### Basic Usage

* Open John Hancock Settings

	1) Enable John Hancock
	2) Select how often you want to refresh the inbox
	3) Input your *Signaturit access token* (Go to your user panel in Signaturit to get the access token)

* Open Contract

	1) **Make a new Contract**
	2) Enter the *recipient*
	3) Select a Contract
	4) Add some signature terms to replace (signature terms are any strings in a Contract that have either backets or curly brackets around them)
	5) Click **Edit Contract**
	6) Scroll to top and click **Request Signature**
	
* Open the Inbox

	1) Click **Make a new Inbox**
	2) Reload (cmd/ctrl + R) (then **don't save**)
	3) Go back to Inbox
	
