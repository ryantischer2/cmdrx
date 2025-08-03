class Cmdrx < Formula
  include Language::Python::Virtualenv

  desc "AI-powered command line troubleshooting tool"
  homepage "https://github.com/cmdrx/cmdrx"
  url "https://github.com/cmdrx/cmdrx/archive/v0.1.0.tar.gz"
  sha256 "SHA256_PLACEHOLDER"  # This would be updated with actual SHA256
  license "MIT"
  head "https://github.com/cmdrx/cmdrx.git", branch: "main"

  depends_on "python@3.11"

  resource "click" do
    url "https://files.pythonhosted.org/packages/96/d3/f04c7bfcf5c1862a2a5b845c6b2b360488cf47af55dfa79c98f6a6bf98b5/click-8.1.7.tar.gz"
    sha256 "ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de"
  end

  resource "rich" do
    url "https://files.pythonhosted.org/packages/a7/ec/4a7d80728bd429f7c0d4d51245287158a1516315cadbb146012439403a9d/rich-13.7.0.tar.gz"
    sha256 "5cb5123b5cf9ee70584244246816e9114227e0b98ad9176eede6ad54bf5403fa"
  end

  resource "requests" do
    url "https://files.pythonhosted.org/packages/9d/be/10918a2eac4ae9f02f6cfe6414b7a155ccd8f7f9d4380d62fd5b955065c3/requests-2.31.0.tar.gz"
    sha256 "942c5a758f98d790eaed1a29cb6eefc7ffb0d1cf7af05c3d2791656dbd6ad1e1"
  end

  resource "keyring" do
    url "https://files.pythonhosted.org/packages/69/cd/889c6569a7e5e9524bc1e423fd2badd967c4a5dcd670c04c2eff92a9d397/keyring-24.3.0.tar.gz"
    sha256 "e730ecffd309658a08ee82535a3b5ec4b4c8669a9be11efb66249d8e0aeb9a25"
  end

  resource "openai" do
    url "https://files.pythonhosted.org/packages/92/91/d5ce5c8894313e60a65ca92dbde6019e34a41c6ebf830f9914ad7c1c8006/openai-1.6.1.tar.gz"
    sha256 "d553f0814a3c71a46e1aa3655cf7b7b45deae7a509f98cfadf4db5c2b9a87da"
  end

  resource "cryptography" do
    url "https://files.pythonhosted.org/packages/13/9c/6a1b6df4e106a4d4c5c79a0e2b72acc8b1cd8bb5b83ed5de7f0f43a0d8c8/cryptography-41.0.7.tar.gz"
    sha256 "13f93ce9bea8016c253b34afc6bd6a75993e5c40672ed5405a9c832f0d4a00bc"
  end

  resource "pydantic" do
    url "https://files.pythonhosted.org/packages/be/c2/7abf5e30154a87b59a6a31c1b854906cf0e8e7c2ad7bb90e8abfe42a8e4b/pydantic-2.5.2.tar.gz"
    sha256 "ff177ba7c9f16d838abb370349c6c5de81b9932142b9c3c6d8b6c1f6a7b9c23"
  end

  resource "textual" do
    url "https://files.pythonhosted.org/packages/5d/42/b26bc3f50d5d09fd69e6db5a2c9c32e4a26ade5a64da7d80fe3ad8fd1c6e/textual-0.45.1.tar.gz"
    sha256 "74a1ffc8e6dfa6cf27e4aa7b70e2a5a8cda32e6c0d5b82a90f568b3e936f3af"
  end

  def install
    virtualenv_install_with_resources

    # Install man page
    man1.install "docs/cmdrx.1"
  end

  test do
    # Test that the command exists and shows help
    assert_match "CmdRx", shell_output("#{bin}/cmdrx --help")
    
    # Test version
    assert_match version.to_s, shell_output("#{bin}/cmdrx --version")
  end
end