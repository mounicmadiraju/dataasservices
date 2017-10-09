(defsystem :exposure
  :author "Sahara Raju"
  :version "0.0.1"
  :license "AL2"
  :description "Expose variables as hookable values on access"
  :serial t
  :components ((:file "package")
               (:file "exposure"))
  :depends-on (:sahara))
