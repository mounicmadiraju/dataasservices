(defproject watcheydog "0.0.1"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :dependencies [[org.clojure/clojure "1.6.0"]
                 [awizo "0.0.11"]
                 [gtk "4.1"]
                 [clj-yaml "0.4.0"]
                 [javax.mail/mail "1.4.3"]]
  :uberjar-name "watcheydog.jar"
  :main ^:skip-aot watcheydog.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
