(in-package :exposure)

(defvar exposed NIL)

(defun find-functions-for-key (kw-name)
  (getf exposed kw-name))

(defun add-expose-hook (kw-name fn)
  (let* ((existing-hooks (getf exposed kw-name))
         (additional-hook (append (list fn) existing-hooks)))
    (setf (getf exposed kw-name) additional-hook)
    exposed))

(defun run-expose-hooks (kw-name value)
  (let ((functions (find-functions-for-key kw-name)))
    (mapcar
     (lambda (fn)
       (funcall fn kw-name value))
       functions)))

(defmacro expose (name &optional actual-name)
  (or (keywordp actual-name)
      (assert (symbolp name)))
  (let ((kw-name (or actual-name (sahara:make-keyword name)))
        (name-sym (gensym)))
    `(let ((,name-sym ,name))
       (run-expose-hooks ,kw-name ,name-sym)
       ,name-sym)))
