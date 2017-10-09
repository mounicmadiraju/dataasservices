hooking
--------

Hooking is a Common Lisp library that allows you to separate actions
you perform on variables from where the variables are located.

The reason you may want to do this is for example, logging and
exporting metrics. Some functions generate values that are interesting
to insert into logging and metrics infrastructure.

Usual way
---------

```lisp
(defun find-things ()
 (let* ((things (sql "SELECT name FROM things"))
        (number-of-things (length things)))
  (log "We have ~A things" number-of-things)
  (graphite-metrics "number_of_things" number-of-things)
  (do-something-with-things things)))
```

What happens here is that all actions we perform on the variable are
grouped together. The `FIND-THINGS` function's actual code becomes
clouded with tangential actions such as logging and metrics gathering.

In reality, what this function does is call
`DO-SOMETHING-WITH-THINGS`, it would be great to retain that clarity
when reading the function but also provide insight into the running
system.

Maybe we can do better.

With hooking
-------------

```lisp
(hooking:add-expose-hook :things
   (lambda (key value)
     (log "We have ~A things" (length value))
     (graphite-metrics "number_of_things" (length value))))

(defun find-things ()
 (let ((things (sql "SELECT name FROM things")))
  (expose things)
  ;; alternatively:
  (expose things :other-name)
  (do-something-with-things things)))
```

In this contrived example, it may look similar but what we've achieved
is the ability to separate out clutter from the original function and
locate it elsewhere. We could, for example, put the hook in a
completely different module.
