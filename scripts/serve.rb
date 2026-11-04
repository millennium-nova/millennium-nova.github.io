# Restart only Jekyll when its configuration changes; keep the IDE running.
require "digest"

$stdout.sync = true
config_files = ["_config.yml"]
fingerprint = -> { config_files.map { |path| File.exist?(path) ? Digest::SHA256.file(path).hexdigest : nil } }
stopping = false
%w[TERM INT].each { |signal| Signal.trap(signal) { stopping = true } }

stop_child = lambda do |pid|
  begin
    Process.kill("TERM", -pid)
  rescue Errno::ESRCH
  end
  deadline = Process.clock_gettime(Process::CLOCK_MONOTONIC) + 10
  loop do
    break if Process.waitpid(pid, Process::WNOHANG)
    if Process.clock_gettime(Process::CLOCK_MONOTONIC) >= deadline
      begin
        Process.kill("KILL", -pid)
      rescue Errno::ESRCH
      end
      Process.waitpid(pid)
      break
    end
    sleep 0.1
  end
end

until stopping
  previous = fingerprint.call
  pid = Process.spawn("bundle", "exec", "jekyll", "serve", "-H", "0.0.0.0", "--watch", "--force_polling", pgroup: true)
  loop do
    if Process.waitpid(pid, Process::WNOHANG)
      exit($?.exitstatus || 1) unless stopping
      break
    end
    if stopping || fingerprint.call != previous
      puts "Configuration changed; restarting Jekyll." unless stopping
      stop_child.call(pid)
      break
    end
    sleep 1
  end
end
