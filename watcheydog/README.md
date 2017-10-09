# watcheydog

watcheydog is a small Maildir watcher which looks for new e-mails and
notifies you of their presence.


## Installation

```shell

$ git clone git@github.com:mounicmadiraju/dataasservices/watcheydog.git
$ cd watcheydog
$ lein uberjar
```

## Usage

Simply start the jar:

```shell
    $ java -jar watcheydog-0.1.0-standalone.jar [args]
```
## Options

watcheydog is configured via /etc/watcheydog.yaml so that file must exist and be
readable by whichever user is running watcheydog.


## Example configuration

```yaml
paths:
- /home/xeno/.mail/
- /home/xeno/.ubnt-mail/

recursive: true
notifier-command: mpg123
notifier-args: /home/xeno/.mutt/notify.mp3
```


### Bugs

Yes.

...

## License

Copyright © 2017 Sahara raju