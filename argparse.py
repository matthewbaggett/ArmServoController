<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US">
<head>
<link rel="icon" href="/cpython/static/hgicon.png" type="image/png" />
<meta name="robots" content="index, nofollow" />
<link rel="stylesheet" href="/cpython/static/style-paper.css" type="text/css" />
<script type="text/javascript" src="/cpython/static/mercurial.js"></script>

<link rel="stylesheet" href="/cpython/highlightcss" type="text/css" />
<title>cpython: e5a09b09bb51 Lib/argparse.py</title>
</head>
<body>

<div class="container">
<div class="menu">
<div class="logo">
<a href="http://hg.python.org">
<img src="/cpython/static/hglogo.png" alt="back to hg.python.org repositories" /></a>
</div>
<ul>
<li><a href="/cpython/shortlog/e5a09b09bb51">log</a></li>
<li><a href="/cpython/graph/e5a09b09bb51">graph</a></li>
<li><a href="/cpython/tags">tags</a></li>
<li><a href="/cpython/branches">branches</a></li>
</ul>
<ul>
<li><a href="/cpython/rev/e5a09b09bb51">changeset</a></li>
<li><a href="/cpython/file/e5a09b09bb51/Lib/">browse</a></li>
</ul>
<ul>
<li class="active">file</li>
<li><a href="/cpython/file/tip/Lib/argparse.py">latest</a></li>
<li><a href="/cpython/diff/e5a09b09bb51/Lib/argparse.py">diff</a></li>
<li><a href="/cpython/comparison/e5a09b09bb51/Lib/argparse.py">comparison</a></li>
<li><a href="/cpython/annotate/e5a09b09bb51/Lib/argparse.py">annotate</a></li>
<li><a href="/cpython/log/e5a09b09bb51/Lib/argparse.py">file log</a></li>
<li><a href="/cpython/raw-file/e5a09b09bb51/Lib/argparse.py">raw</a></li>
</ul>
<ul>
<li><a href="/cpython/help">help</a></li>
</ul>
</div>

<div class="main">
<h2 class="breadcrumb"><a href="/">Mercurial</a> &gt; <a href="/cpython">cpython</a> </h2>
<h3>view Lib/argparse.py @ 89687:e5a09b09bb51</h3>

<form class="search" action="/cpython/log">

<p><input name="rev" id="search1" type="text" size="30" /></p>
<div id="hint">Find changesets by keywords (author, files, the commit message), revision
number or hash, or <a href="/cpython/help/revsets">revset expression</a>.</div>
</form>

<div class="description">fix ctypes test alignment assumptions (closes #20946)

Patch by Andreas Schwab.</a> [<a href="http://bugs.python.org/20946" class="issuelink">#20946</a>]</div>

<table id="changesetEntry">
<tr>
 <th class="author">author</th>
 <td class="author">&#66;&#101;&#110;&#106;&#97;&#109;&#105;&#110;&#32;&#80;&#101;&#116;&#101;&#114;&#115;&#111;&#110;&#32;&#60;&#98;&#101;&#110;&#106;&#97;&#109;&#105;&#110;&#64;&#112;&#121;&#116;&#104;&#111;&#110;&#46;&#111;&#114;&#103;&#62;</td>
</tr>
<tr>
 <th class="date">date</th>
 <td class="date age">Sun, 16 Mar 2014 10:07:26 +0100</td>
</tr>
<tr>
 <th class="author">parents</th>
 <td class="author"><a href="/cpython/file/8f847f66a49f/Lib/argparse.py">8f847f66a49f</a> </td>
</tr>
<tr>
 <th class="author">children</th>
 <td class="author"></td>
</tr>
</table>

<div class="overflow">
<div class="sourcefirst linewraptoggle">line wrap: <a class="linewraplink" href="javascript:toggleLinewrap()">on</a></div>
<div class="sourcefirst"> line source</div>
<pre class="sourcelines stripes4 wrap">
<span id="l1"><span class="c"># Author: Steven J. Bethard &lt;steven.bethard@gmail.com&gt;.</span></span><a href="#l1"></a>
<span id="l2"></span><a href="#l2"></a>
<span id="l3"><span class="sd">&quot;&quot;&quot;Command-line parsing library</span></span><a href="#l3"></a>
<span id="l4"></span><a href="#l4"></a>
<span id="l5"><span class="sd">This module is an optparse-inspired command-line parsing library that:</span></span><a href="#l5"></a>
<span id="l6"></span><a href="#l6"></a>
<span id="l7"><span class="sd">    - handles both optional and positional arguments</span></span><a href="#l7"></a>
<span id="l8"><span class="sd">    - produces highly informative usage messages</span></span><a href="#l8"></a>
<span id="l9"><span class="sd">    - supports parsers that dispatch to sub-parsers</span></span><a href="#l9"></a>
<span id="l10"></span><a href="#l10"></a>
<span id="l11"><span class="sd">The following is a simple usage example that sums integers from the</span></span><a href="#l11"></a>
<span id="l12"><span class="sd">command-line and writes the result to a file::</span></span><a href="#l12"></a>
<span id="l13"></span><a href="#l13"></a>
<span id="l14"><span class="sd">    parser = argparse.ArgumentParser(</span></span><a href="#l14"></a>
<span id="l15"><span class="sd">        description=&#39;sum the integers at the command line&#39;)</span></span><a href="#l15"></a>
<span id="l16"><span class="sd">    parser.add_argument(</span></span><a href="#l16"></a>
<span id="l17"><span class="sd">        &#39;integers&#39;, metavar=&#39;int&#39;, nargs=&#39;+&#39;, type=int,</span></span><a href="#l17"></a>
<span id="l18"><span class="sd">        help=&#39;an integer to be summed&#39;)</span></span><a href="#l18"></a>
<span id="l19"><span class="sd">    parser.add_argument(</span></span><a href="#l19"></a>
<span id="l20"><span class="sd">        &#39;--log&#39;, default=sys.stdout, type=argparse.FileType(&#39;w&#39;),</span></span><a href="#l20"></a>
<span id="l21"><span class="sd">        help=&#39;the file where the sum should be written&#39;)</span></span><a href="#l21"></a>
<span id="l22"><span class="sd">    args = parser.parse_args()</span></span><a href="#l22"></a>
<span id="l23"><span class="sd">    args.log.write(&#39;%s&#39; % sum(args.integers))</span></span><a href="#l23"></a>
<span id="l24"><span class="sd">    args.log.close()</span></span><a href="#l24"></a>
<span id="l25"></span><a href="#l25"></a>
<span id="l26"><span class="sd">The module contains the following public classes:</span></span><a href="#l26"></a>
<span id="l27"></span><a href="#l27"></a>
<span id="l28"><span class="sd">    - ArgumentParser -- The main entry point for command-line parsing. As the</span></span><a href="#l28"></a>
<span id="l29"><span class="sd">        example above shows, the add_argument() method is used to populate</span></span><a href="#l29"></a>
<span id="l30"><span class="sd">        the parser with actions for optional and positional arguments. Then</span></span><a href="#l30"></a>
<span id="l31"><span class="sd">        the parse_args() method is invoked to convert the args at the</span></span><a href="#l31"></a>
<span id="l32"><span class="sd">        command-line into an object with attributes.</span></span><a href="#l32"></a>
<span id="l33"></span><a href="#l33"></a>
<span id="l34"><span class="sd">    - ArgumentError -- The exception raised by ArgumentParser objects when</span></span><a href="#l34"></a>
<span id="l35"><span class="sd">        there are errors with the parser&#39;s actions. Errors raised while</span></span><a href="#l35"></a>
<span id="l36"><span class="sd">        parsing the command-line are caught by ArgumentParser and emitted</span></span><a href="#l36"></a>
<span id="l37"><span class="sd">        as command-line messages.</span></span><a href="#l37"></a>
<span id="l38"></span><a href="#l38"></a>
<span id="l39"><span class="sd">    - FileType -- A factory for defining types of files to be created. As the</span></span><a href="#l39"></a>
<span id="l40"><span class="sd">        example above shows, instances of FileType are typically passed as</span></span><a href="#l40"></a>
<span id="l41"><span class="sd">        the type= argument of add_argument() calls.</span></span><a href="#l41"></a>
<span id="l42"></span><a href="#l42"></a>
<span id="l43"><span class="sd">    - Action -- The base class for parser actions. Typically actions are</span></span><a href="#l43"></a>
<span id="l44"><span class="sd">        selected by passing strings like &#39;store_true&#39; or &#39;append_const&#39; to</span></span><a href="#l44"></a>
<span id="l45"><span class="sd">        the action= argument of add_argument(). However, for greater</span></span><a href="#l45"></a>
<span id="l46"><span class="sd">        customization of ArgumentParser actions, subclasses of Action may</span></span><a href="#l46"></a>
<span id="l47"><span class="sd">        be defined and passed as the action= argument.</span></span><a href="#l47"></a>
<span id="l48"></span><a href="#l48"></a>
<span id="l49"><span class="sd">    - HelpFormatter, RawDescriptionHelpFormatter, RawTextHelpFormatter,</span></span><a href="#l49"></a>
<span id="l50"><span class="sd">        ArgumentDefaultsHelpFormatter -- Formatter classes which</span></span><a href="#l50"></a>
<span id="l51"><span class="sd">        may be passed as the formatter_class= argument to the</span></span><a href="#l51"></a>
<span id="l52"><span class="sd">        ArgumentParser constructor. HelpFormatter is the default,</span></span><a href="#l52"></a>
<span id="l53"><span class="sd">        RawDescriptionHelpFormatter and RawTextHelpFormatter tell the parser</span></span><a href="#l53"></a>
<span id="l54"><span class="sd">        not to change the formatting for help text, and</span></span><a href="#l54"></a>
<span id="l55"><span class="sd">        ArgumentDefaultsHelpFormatter adds information about argument defaults</span></span><a href="#l55"></a>
<span id="l56"><span class="sd">        to the help.</span></span><a href="#l56"></a>
<span id="l57"></span><a href="#l57"></a>
<span id="l58"><span class="sd">All other classes in this module are considered implementation details.</span></span><a href="#l58"></a>
<span id="l59"><span class="sd">(Also note that HelpFormatter and RawDescriptionHelpFormatter are only</span></span><a href="#l59"></a>
<span id="l60"><span class="sd">considered public as object names -- the API of the formatter objects is</span></span><a href="#l60"></a>
<span id="l61"><span class="sd">still considered an implementation detail.)</span></span><a href="#l61"></a>
<span id="l62"><span class="sd">&quot;&quot;&quot;</span></span><a href="#l62"></a>
<span id="l63"></span><a href="#l63"></a>
<span id="l64"><span class="n">__version__</span> <span class="o">=</span> <span class="s">&#39;1.1&#39;</span></span><a href="#l64"></a>
<span id="l65"><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span></span><a href="#l65"></a>
<span id="l66">    <span class="s">&#39;ArgumentParser&#39;</span><span class="p">,</span></span><a href="#l66"></a>
<span id="l67">    <span class="s">&#39;ArgumentError&#39;</span><span class="p">,</span></span><a href="#l67"></a>
<span id="l68">    <span class="s">&#39;ArgumentTypeError&#39;</span><span class="p">,</span></span><a href="#l68"></a>
<span id="l69">    <span class="s">&#39;FileType&#39;</span><span class="p">,</span></span><a href="#l69"></a>
<span id="l70">    <span class="s">&#39;HelpFormatter&#39;</span><span class="p">,</span></span><a href="#l70"></a>
<span id="l71">    <span class="s">&#39;ArgumentDefaultsHelpFormatter&#39;</span><span class="p">,</span></span><a href="#l71"></a>
<span id="l72">    <span class="s">&#39;RawDescriptionHelpFormatter&#39;</span><span class="p">,</span></span><a href="#l72"></a>
<span id="l73">    <span class="s">&#39;RawTextHelpFormatter&#39;</span><span class="p">,</span></span><a href="#l73"></a>
<span id="l74">    <span class="s">&#39;Namespace&#39;</span><span class="p">,</span></span><a href="#l74"></a>
<span id="l75">    <span class="s">&#39;Action&#39;</span><span class="p">,</span></span><a href="#l75"></a>
<span id="l76">    <span class="s">&#39;ONE_OR_MORE&#39;</span><span class="p">,</span></span><a href="#l76"></a>
<span id="l77">    <span class="s">&#39;OPTIONAL&#39;</span><span class="p">,</span></span><a href="#l77"></a>
<span id="l78">    <span class="s">&#39;PARSER&#39;</span><span class="p">,</span></span><a href="#l78"></a>
<span id="l79">    <span class="s">&#39;REMAINDER&#39;</span><span class="p">,</span></span><a href="#l79"></a>
<span id="l80">    <span class="s">&#39;SUPPRESS&#39;</span><span class="p">,</span></span><a href="#l80"></a>
<span id="l81">    <span class="s">&#39;ZERO_OR_MORE&#39;</span><span class="p">,</span></span><a href="#l81"></a>
<span id="l82"><span class="p">]</span></span><a href="#l82"></a>
<span id="l83"></span><a href="#l83"></a>
<span id="l84"></span><a href="#l84"></a>
<span id="l85"><span class="kn">import</span> <span class="nn">collections</span> <span class="kn">as</span> <span class="nn">_collections</span></span><a href="#l85"></a>
<span id="l86"><span class="kn">import</span> <span class="nn">copy</span> <span class="kn">as</span> <span class="nn">_copy</span></span><a href="#l86"></a>
<span id="l87"><span class="kn">import</span> <span class="nn">os</span> <span class="kn">as</span> <span class="nn">_os</span></span><a href="#l87"></a>
<span id="l88"><span class="kn">import</span> <span class="nn">re</span> <span class="kn">as</span> <span class="nn">_re</span></span><a href="#l88"></a>
<span id="l89"><span class="kn">import</span> <span class="nn">sys</span> <span class="kn">as</span> <span class="nn">_sys</span></span><a href="#l89"></a>
<span id="l90"><span class="kn">import</span> <span class="nn">textwrap</span> <span class="kn">as</span> <span class="nn">_textwrap</span></span><a href="#l90"></a>
<span id="l91"></span><a href="#l91"></a>
<span id="l92"><span class="kn">from</span> <span class="nn">gettext</span> <span class="kn">import</span> <span class="n">gettext</span> <span class="k">as</span> <span class="n">_</span></span><a href="#l92"></a>
<span id="l93"></span><a href="#l93"></a>
<span id="l94"></span><a href="#l94"></a>
<span id="l95"><span class="k">def</span> <span class="nf">_callable</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span></span><a href="#l95"></a>
<span id="l96">    <span class="k">return</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="s">&#39;__call__&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="s">&#39;__bases__&#39;</span><span class="p">)</span></span><a href="#l96"></a>
<span id="l97"></span><a href="#l97"></a>
<span id="l98"></span><a href="#l98"></a>
<span id="l99"><span class="n">SUPPRESS</span> <span class="o">=</span> <span class="s">&#39;==SUPPRESS==&#39;</span></span><a href="#l99"></a>
<span id="l100"></span><a href="#l100"></a>
<span id="l101"><span class="n">OPTIONAL</span> <span class="o">=</span> <span class="s">&#39;?&#39;</span></span><a href="#l101"></a>
<span id="l102"><span class="n">ZERO_OR_MORE</span> <span class="o">=</span> <span class="s">&#39;*&#39;</span></span><a href="#l102"></a>
<span id="l103"><span class="n">ONE_OR_MORE</span> <span class="o">=</span> <span class="s">&#39;+&#39;</span></span><a href="#l103"></a>
<span id="l104"><span class="n">PARSER</span> <span class="o">=</span> <span class="s">&#39;A...&#39;</span></span><a href="#l104"></a>
<span id="l105"><span class="n">REMAINDER</span> <span class="o">=</span> <span class="s">&#39;...&#39;</span></span><a href="#l105"></a>
<span id="l106"><span class="n">_UNRECOGNIZED_ARGS_ATTR</span> <span class="o">=</span> <span class="s">&#39;_unrecognized_args&#39;</span></span><a href="#l106"></a>
<span id="l107"></span><a href="#l107"></a>
<span id="l108"><span class="c"># =============================</span></span><a href="#l108"></a>
<span id="l109"><span class="c"># Utility functions and classes</span></span><a href="#l109"></a>
<span id="l110"><span class="c"># =============================</span></span><a href="#l110"></a>
<span id="l111"></span><a href="#l111"></a>
<span id="l112"><span class="k">class</span> <span class="nc">_AttributeHolder</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l112"></a>
<span id="l113">    <span class="sd">&quot;&quot;&quot;Abstract base class that provides __repr__.</span></span><a href="#l113"></a>
<span id="l114"></span><a href="#l114"></a>
<span id="l115"><span class="sd">    The __repr__ method returns a string in the format::</span></span><a href="#l115"></a>
<span id="l116"><span class="sd">        ClassName(attr=name, attr=name, ...)</span></span><a href="#l116"></a>
<span id="l117"><span class="sd">    The attributes are determined either by a class-level attribute,</span></span><a href="#l117"></a>
<span id="l118"><span class="sd">    &#39;_kwarg_names&#39;, or by inspecting the instance __dict__.</span></span><a href="#l118"></a>
<span id="l119"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l119"></a>
<span id="l120"></span><a href="#l120"></a>
<span id="l121">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l121"></a>
<span id="l122">        <span class="n">type_name</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__name__</span></span><a href="#l122"></a>
<span id="l123">        <span class="n">arg_strings</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l123"></a>
<span id="l124">        <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_args</span><span class="p">():</span></span><a href="#l124"></a>
<span id="l125">            <span class="n">arg_strings</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="n">arg</span><span class="p">))</span></span><a href="#l125"></a>
<span id="l126">        <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_kwargs</span><span class="p">():</span></span><a href="#l126"></a>
<span id="l127">            <span class="n">arg_strings</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s">=</span><span class="si">%r</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">value</span><span class="p">))</span></span><a href="#l127"></a>
<span id="l128">        <span class="k">return</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">(</span><span class="si">%s</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">type_name</span><span class="p">,</span> <span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">arg_strings</span><span class="p">))</span></span><a href="#l128"></a>
<span id="l129"></span><a href="#l129"></a>
<span id="l130">    <span class="k">def</span> <span class="nf">_get_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l130"></a>
<span id="l131">        <span class="k">return</span> <span class="nb">sorted</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__dict__</span><span class="o">.</span><span class="n">items</span><span class="p">())</span></span><a href="#l131"></a>
<span id="l132"></span><a href="#l132"></a>
<span id="l133">    <span class="k">def</span> <span class="nf">_get_args</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l133"></a>
<span id="l134">        <span class="k">return</span> <span class="p">[]</span></span><a href="#l134"></a>
<span id="l135"></span><a href="#l135"></a>
<span id="l136"></span><a href="#l136"></a>
<span id="l137"><span class="k">def</span> <span class="nf">_ensure_value</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span></span><a href="#l137"></a>
<span id="l138">    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l138"></a>
<span id="l139">        <span class="nb">setattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span></span><a href="#l139"></a>
<span id="l140">    <span class="k">return</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span></span><a href="#l140"></a>
<span id="l141"></span><a href="#l141"></a>
<span id="l142"></span><a href="#l142"></a>
<span id="l143"><span class="c"># ===============</span></span><a href="#l143"></a>
<span id="l144"><span class="c"># Formatting Help</span></span><a href="#l144"></a>
<span id="l145"><span class="c"># ===============</span></span><a href="#l145"></a>
<span id="l146"></span><a href="#l146"></a>
<span id="l147"><span class="k">class</span> <span class="nc">HelpFormatter</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l147"></a>
<span id="l148">    <span class="sd">&quot;&quot;&quot;Formatter for generating usage messages and argument help strings.</span></span><a href="#l148"></a>
<span id="l149"></span><a href="#l149"></a>
<span id="l150"><span class="sd">    Only the name of this class is considered a public API. All the methods</span></span><a href="#l150"></a>
<span id="l151"><span class="sd">    provided by the class are considered an implementation detail.</span></span><a href="#l151"></a>
<span id="l152"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l152"></a>
<span id="l153"></span><a href="#l153"></a>
<span id="l154">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l154"></a>
<span id="l155">                 <span class="n">prog</span><span class="p">,</span></span><a href="#l155"></a>
<span id="l156">                 <span class="n">indent_increment</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span></span><a href="#l156"></a>
<span id="l157">                 <span class="n">max_help_position</span><span class="o">=</span><span class="mi">24</span><span class="p">,</span></span><a href="#l157"></a>
<span id="l158">                 <span class="n">width</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l158"></a>
<span id="l159"></span><a href="#l159"></a>
<span id="l160">        <span class="c"># default setting for width</span></span><a href="#l160"></a>
<span id="l161">        <span class="k">if</span> <span class="n">width</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l161"></a>
<span id="l162">            <span class="k">try</span><span class="p">:</span></span><a href="#l162"></a>
<span id="l163">                <span class="n">width</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">_os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s">&#39;COLUMNS&#39;</span><span class="p">])</span></span><a href="#l163"></a>
<span id="l164">            <span class="k">except</span> <span class="p">(</span><span class="ne">KeyError</span><span class="p">,</span> <span class="ne">ValueError</span><span class="p">):</span></span><a href="#l164"></a>
<span id="l165">                <span class="n">width</span> <span class="o">=</span> <span class="mi">80</span></span><a href="#l165"></a>
<span id="l166">            <span class="n">width</span> <span class="o">-=</span> <span class="mi">2</span></span><a href="#l166"></a>
<span id="l167"></span><a href="#l167"></a>
<span id="l168">        <span class="bp">self</span><span class="o">.</span><span class="n">_prog</span> <span class="o">=</span> <span class="n">prog</span></span><a href="#l168"></a>
<span id="l169">        <span class="bp">self</span><span class="o">.</span><span class="n">_indent_increment</span> <span class="o">=</span> <span class="n">indent_increment</span></span><a href="#l169"></a>
<span id="l170">        <span class="bp">self</span><span class="o">.</span><span class="n">_max_help_position</span> <span class="o">=</span> <span class="n">max_help_position</span></span><a href="#l170"></a>
<span id="l171">        <span class="bp">self</span><span class="o">.</span><span class="n">_max_help_position</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">max_help_position</span><span class="p">,</span></span><a href="#l171"></a>
<span id="l172">                                      <span class="nb">max</span><span class="p">(</span><span class="n">width</span> <span class="o">-</span> <span class="mi">20</span><span class="p">,</span> <span class="n">indent_increment</span> <span class="o">*</span> <span class="mi">2</span><span class="p">))</span></span><a href="#l172"></a>
<span id="l173">        <span class="bp">self</span><span class="o">.</span><span class="n">_width</span> <span class="o">=</span> <span class="n">width</span></span><a href="#l173"></a>
<span id="l174"></span><a href="#l174"></a>
<span id="l175">        <span class="bp">self</span><span class="o">.</span><span class="n">_current_indent</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l175"></a>
<span id="l176">        <span class="bp">self</span><span class="o">.</span><span class="n">_level</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l176"></a>
<span id="l177">        <span class="bp">self</span><span class="o">.</span><span class="n">_action_max_length</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l177"></a>
<span id="l178"></span><a href="#l178"></a>
<span id="l179">        <span class="bp">self</span><span class="o">.</span><span class="n">_root_section</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_Section</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l179"></a>
<span id="l180">        <span class="bp">self</span><span class="o">.</span><span class="n">_current_section</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root_section</span></span><a href="#l180"></a>
<span id="l181"></span><a href="#l181"></a>
<span id="l182">        <span class="bp">self</span><span class="o">.</span><span class="n">_whitespace_matcher</span> <span class="o">=</span> <span class="n">_re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;\s+&#39;</span><span class="p">)</span></span><a href="#l182"></a>
<span id="l183">        <span class="bp">self</span><span class="o">.</span><span class="n">_long_break_matcher</span> <span class="o">=</span> <span class="n">_re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;\n\n\n+&#39;</span><span class="p">)</span></span><a href="#l183"></a>
<span id="l184"></span><a href="#l184"></a>
<span id="l185">    <span class="c"># ===============================</span></span><a href="#l185"></a>
<span id="l186">    <span class="c"># Section and indentation methods</span></span><a href="#l186"></a>
<span id="l187">    <span class="c"># ===============================</span></span><a href="#l187"></a>
<span id="l188">    <span class="k">def</span> <span class="nf">_indent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l188"></a>
<span id="l189">        <span class="bp">self</span><span class="o">.</span><span class="n">_current_indent</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_indent_increment</span></span><a href="#l189"></a>
<span id="l190">        <span class="bp">self</span><span class="o">.</span><span class="n">_level</span> <span class="o">+=</span> <span class="mi">1</span></span><a href="#l190"></a>
<span id="l191"></span><a href="#l191"></a>
<span id="l192">    <span class="k">def</span> <span class="nf">_dedent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l192"></a>
<span id="l193">        <span class="bp">self</span><span class="o">.</span><span class="n">_current_indent</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_indent_increment</span></span><a href="#l193"></a>
<span id="l194">        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_indent</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">,</span> <span class="s">&#39;Indent decreased below 0.&#39;</span></span><a href="#l194"></a>
<span id="l195">        <span class="bp">self</span><span class="o">.</span><span class="n">_level</span> <span class="o">-=</span> <span class="mi">1</span></span><a href="#l195"></a>
<span id="l196"></span><a href="#l196"></a>
<span id="l197">    <span class="k">class</span> <span class="nc">_Section</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l197"></a>
<span id="l198"></span><a href="#l198"></a>
<span id="l199">        <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">formatter</span><span class="p">,</span> <span class="n">parent</span><span class="p">,</span> <span class="n">heading</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l199"></a>
<span id="l200">            <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span> <span class="o">=</span> <span class="n">formatter</span></span><a href="#l200"></a>
<span id="l201">            <span class="bp">self</span><span class="o">.</span><span class="n">parent</span> <span class="o">=</span> <span class="n">parent</span></span><a href="#l201"></a>
<span id="l202">            <span class="bp">self</span><span class="o">.</span><span class="n">heading</span> <span class="o">=</span> <span class="n">heading</span></span><a href="#l202"></a>
<span id="l203">            <span class="bp">self</span><span class="o">.</span><span class="n">items</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l203"></a>
<span id="l204"></span><a href="#l204"></a>
<span id="l205">        <span class="k">def</span> <span class="nf">format_help</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l205"></a>
<span id="l206">            <span class="c"># format the indented section</span></span><a href="#l206"></a>
<span id="l207">            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">parent</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l207"></a>
<span id="l208">                <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span><span class="o">.</span><span class="n">_indent</span><span class="p">()</span></span><a href="#l208"></a>
<span id="l209">            <span class="n">join</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span><span class="o">.</span><span class="n">_join_parts</span></span><a href="#l209"></a>
<span id="l210">            <span class="k">for</span> <span class="n">func</span><span class="p">,</span> <span class="n">args</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">items</span><span class="p">:</span></span><a href="#l210"></a>
<span id="l211">                <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span></span><a href="#l211"></a>
<span id="l212">            <span class="n">item_help</span> <span class="o">=</span> <span class="n">join</span><span class="p">([</span><span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span> <span class="k">for</span> <span class="n">func</span><span class="p">,</span> <span class="n">args</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">items</span><span class="p">])</span></span><a href="#l212"></a>
<span id="l213">            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">parent</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l213"></a>
<span id="l214">                <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span><span class="o">.</span><span class="n">_dedent</span><span class="p">()</span></span><a href="#l214"></a>
<span id="l215"></span><a href="#l215"></a>
<span id="l216">            <span class="c"># return nothing if the section was empty</span></span><a href="#l216"></a>
<span id="l217">            <span class="k">if</span> <span class="ow">not</span> <span class="n">item_help</span><span class="p">:</span></span><a href="#l217"></a>
<span id="l218">                <span class="k">return</span> <span class="s">&#39;&#39;</span></span><a href="#l218"></a>
<span id="l219"></span><a href="#l219"></a>
<span id="l220">            <span class="c"># add the heading if the section was non-empty</span></span><a href="#l220"></a>
<span id="l221">            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">heading</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">SUPPRESS</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">heading</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l221"></a>
<span id="l222">                <span class="n">current_indent</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span><span class="o">.</span><span class="n">_current_indent</span></span><a href="#l222"></a>
<span id="l223">                <span class="n">heading</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%*s%s</span><span class="s">:</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">current_indent</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">heading</span><span class="p">)</span></span><a href="#l223"></a>
<span id="l224">            <span class="k">else</span><span class="p">:</span></span><a href="#l224"></a>
<span id="l225">                <span class="n">heading</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></span><a href="#l225"></a>
<span id="l226"></span><a href="#l226"></a>
<span id="l227">            <span class="c"># join the section-initial newline, the heading and the help</span></span><a href="#l227"></a>
<span id="l228">            <span class="k">return</span> <span class="n">join</span><span class="p">([</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">heading</span><span class="p">,</span> <span class="n">item_help</span><span class="p">,</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">])</span></span><a href="#l228"></a>
<span id="l229"></span><a href="#l229"></a>
<span id="l230">    <span class="k">def</span> <span class="nf">_add_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="n">args</span><span class="p">):</span></span><a href="#l230"></a>
<span id="l231">        <span class="bp">self</span><span class="o">.</span><span class="n">_current_section</span><span class="o">.</span><span class="n">items</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">func</span><span class="p">,</span> <span class="n">args</span><span class="p">))</span></span><a href="#l231"></a>
<span id="l232"></span><a href="#l232"></a>
<span id="l233">    <span class="c"># ========================</span></span><a href="#l233"></a>
<span id="l234">    <span class="c"># Message building methods</span></span><a href="#l234"></a>
<span id="l235">    <span class="c"># ========================</span></span><a href="#l235"></a>
<span id="l236">    <span class="k">def</span> <span class="nf">start_section</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">heading</span><span class="p">):</span></span><a href="#l236"></a>
<span id="l237">        <span class="bp">self</span><span class="o">.</span><span class="n">_indent</span><span class="p">()</span></span><a href="#l237"></a>
<span id="l238">        <span class="n">section</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_Section</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_section</span><span class="p">,</span> <span class="n">heading</span><span class="p">)</span></span><a href="#l238"></a>
<span id="l239">        <span class="bp">self</span><span class="o">.</span><span class="n">_add_item</span><span class="p">(</span><span class="n">section</span><span class="o">.</span><span class="n">format_help</span><span class="p">,</span> <span class="p">[])</span></span><a href="#l239"></a>
<span id="l240">        <span class="bp">self</span><span class="o">.</span><span class="n">_current_section</span> <span class="o">=</span> <span class="n">section</span></span><a href="#l240"></a>
<span id="l241"></span><a href="#l241"></a>
<span id="l242">    <span class="k">def</span> <span class="nf">end_section</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l242"></a>
<span id="l243">        <span class="bp">self</span><span class="o">.</span><span class="n">_current_section</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_section</span><span class="o">.</span><span class="n">parent</span></span><a href="#l243"></a>
<span id="l244">        <span class="bp">self</span><span class="o">.</span><span class="n">_dedent</span><span class="p">()</span></span><a href="#l244"></a>
<span id="l245"></span><a href="#l245"></a>
<span id="l246">    <span class="k">def</span> <span class="nf">add_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">):</span></span><a href="#l246"></a>
<span id="l247">        <span class="k">if</span> <span class="n">text</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">SUPPRESS</span> <span class="ow">and</span> <span class="n">text</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l247"></a>
<span id="l248">            <span class="bp">self</span><span class="o">.</span><span class="n">_add_item</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_format_text</span><span class="p">,</span> <span class="p">[</span><span class="n">text</span><span class="p">])</span></span><a href="#l248"></a>
<span id="l249"></span><a href="#l249"></a>
<span id="l250">    <span class="k">def</span> <span class="nf">add_usage</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">usage</span><span class="p">,</span> <span class="n">actions</span><span class="p">,</span> <span class="n">groups</span><span class="p">,</span> <span class="n">prefix</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l250"></a>
<span id="l251">        <span class="k">if</span> <span class="n">usage</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">SUPPRESS</span><span class="p">:</span></span><a href="#l251"></a>
<span id="l252">            <span class="n">args</span> <span class="o">=</span> <span class="n">usage</span><span class="p">,</span> <span class="n">actions</span><span class="p">,</span> <span class="n">groups</span><span class="p">,</span> <span class="n">prefix</span></span><a href="#l252"></a>
<span id="l253">            <span class="bp">self</span><span class="o">.</span><span class="n">_add_item</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_format_usage</span><span class="p">,</span> <span class="n">args</span><span class="p">)</span></span><a href="#l253"></a>
<span id="l254"></span><a href="#l254"></a>
<span id="l255">    <span class="k">def</span> <span class="nf">add_argument</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l255"></a>
<span id="l256">        <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">help</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">SUPPRESS</span><span class="p">:</span></span><a href="#l256"></a>
<span id="l257"></span><a href="#l257"></a>
<span id="l258">            <span class="c"># find all invocations</span></span><a href="#l258"></a>
<span id="l259">            <span class="n">get_invocation</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_action_invocation</span></span><a href="#l259"></a>
<span id="l260">            <span class="n">invocations</span> <span class="o">=</span> <span class="p">[</span><span class="n">get_invocation</span><span class="p">(</span><span class="n">action</span><span class="p">)]</span></span><a href="#l260"></a>
<span id="l261">            <span class="k">for</span> <span class="n">subaction</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_iter_indented_subactions</span><span class="p">(</span><span class="n">action</span><span class="p">):</span></span><a href="#l261"></a>
<span id="l262">                <span class="n">invocations</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">get_invocation</span><span class="p">(</span><span class="n">subaction</span><span class="p">))</span></span><a href="#l262"></a>
<span id="l263"></span><a href="#l263"></a>
<span id="l264">            <span class="c"># update the maximum item length</span></span><a href="#l264"></a>
<span id="l265">            <span class="n">invocation_length</span> <span class="o">=</span> <span class="nb">max</span><span class="p">([</span><span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">invocations</span><span class="p">])</span></span><a href="#l265"></a>
<span id="l266">            <span class="n">action_length</span> <span class="o">=</span> <span class="n">invocation_length</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_indent</span></span><a href="#l266"></a>
<span id="l267">            <span class="bp">self</span><span class="o">.</span><span class="n">_action_max_length</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_action_max_length</span><span class="p">,</span></span><a href="#l267"></a>
<span id="l268">                                          <span class="n">action_length</span><span class="p">)</span></span><a href="#l268"></a>
<span id="l269"></span><a href="#l269"></a>
<span id="l270">            <span class="c"># add the item to the list</span></span><a href="#l270"></a>
<span id="l271">            <span class="bp">self</span><span class="o">.</span><span class="n">_add_item</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_format_action</span><span class="p">,</span> <span class="p">[</span><span class="n">action</span><span class="p">])</span></span><a href="#l271"></a>
<span id="l272"></span><a href="#l272"></a>
<span id="l273">    <span class="k">def</span> <span class="nf">add_arguments</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">actions</span><span class="p">):</span></span><a href="#l273"></a>
<span id="l274">        <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">actions</span><span class="p">:</span></span><a href="#l274"></a>
<span id="l275">            <span class="bp">self</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l275"></a>
<span id="l276"></span><a href="#l276"></a>
<span id="l277">    <span class="c"># =======================</span></span><a href="#l277"></a>
<span id="l278">    <span class="c"># Help-formatting methods</span></span><a href="#l278"></a>
<span id="l279">    <span class="c"># =======================</span></span><a href="#l279"></a>
<span id="l280">    <span class="k">def</span> <span class="nf">format_help</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l280"></a>
<span id="l281">        <span class="n">help</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root_section</span><span class="o">.</span><span class="n">format_help</span><span class="p">()</span></span><a href="#l281"></a>
<span id="l282">        <span class="k">if</span> <span class="n">help</span><span class="p">:</span></span><a href="#l282"></a>
<span id="l283">            <span class="n">help</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_long_break_matcher</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n\n</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">help</span><span class="p">)</span></span><a href="#l283"></a>
<span id="l284">            <span class="n">help</span> <span class="o">=</span> <span class="n">help</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span></span><a href="#l284"></a>
<span id="l285">        <span class="k">return</span> <span class="n">help</span></span><a href="#l285"></a>
<span id="l286"></span><a href="#l286"></a>
<span id="l287">    <span class="k">def</span> <span class="nf">_join_parts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">part_strings</span><span class="p">):</span></span><a href="#l287"></a>
<span id="l288">        <span class="k">return</span> <span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">part</span></span><a href="#l288"></a>
<span id="l289">                        <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">part_strings</span></span><a href="#l289"></a>
<span id="l290">                        <span class="k">if</span> <span class="n">part</span> <span class="ow">and</span> <span class="n">part</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">SUPPRESS</span><span class="p">])</span></span><a href="#l290"></a>
<span id="l291"></span><a href="#l291"></a>
<span id="l292">    <span class="k">def</span> <span class="nf">_format_usage</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">usage</span><span class="p">,</span> <span class="n">actions</span><span class="p">,</span> <span class="n">groups</span><span class="p">,</span> <span class="n">prefix</span><span class="p">):</span></span><a href="#l292"></a>
<span id="l293">        <span class="k">if</span> <span class="n">prefix</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l293"></a>
<span id="l294">            <span class="n">prefix</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;usage: &#39;</span><span class="p">)</span></span><a href="#l294"></a>
<span id="l295"></span><a href="#l295"></a>
<span id="l296">        <span class="c"># if usage is specified, use that</span></span><a href="#l296"></a>
<span id="l297">        <span class="k">if</span> <span class="n">usage</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l297"></a>
<span id="l298">            <span class="n">usage</span> <span class="o">=</span> <span class="n">usage</span> <span class="o">%</span> <span class="nb">dict</span><span class="p">(</span><span class="n">prog</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_prog</span><span class="p">)</span></span><a href="#l298"></a>
<span id="l299"></span><a href="#l299"></a>
<span id="l300">        <span class="c"># if no optionals or positionals are available, usage is just prog</span></span><a href="#l300"></a>
<span id="l301">        <span class="k">elif</span> <span class="n">usage</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">actions</span><span class="p">:</span></span><a href="#l301"></a>
<span id="l302">            <span class="n">usage</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%(prog)s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="nb">dict</span><span class="p">(</span><span class="n">prog</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_prog</span><span class="p">)</span></span><a href="#l302"></a>
<span id="l303"></span><a href="#l303"></a>
<span id="l304">        <span class="c"># if optionals and positionals are available, calculate usage</span></span><a href="#l304"></a>
<span id="l305">        <span class="k">elif</span> <span class="n">usage</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l305"></a>
<span id="l306">            <span class="n">prog</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%(prog)s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="nb">dict</span><span class="p">(</span><span class="n">prog</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_prog</span><span class="p">)</span></span><a href="#l306"></a>
<span id="l307"></span><a href="#l307"></a>
<span id="l308">            <span class="c"># split optionals from positionals</span></span><a href="#l308"></a>
<span id="l309">            <span class="n">optionals</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l309"></a>
<span id="l310">            <span class="n">positionals</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l310"></a>
<span id="l311">            <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">actions</span><span class="p">:</span></span><a href="#l311"></a>
<span id="l312">                <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">:</span></span><a href="#l312"></a>
<span id="l313">                    <span class="n">optionals</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l313"></a>
<span id="l314">                <span class="k">else</span><span class="p">:</span></span><a href="#l314"></a>
<span id="l315">                    <span class="n">positionals</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l315"></a>
<span id="l316"></span><a href="#l316"></a>
<span id="l317">            <span class="c"># build full usage string</span></span><a href="#l317"></a>
<span id="l318">            <span class="n">format</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_actions_usage</span></span><a href="#l318"></a>
<span id="l319">            <span class="n">action_usage</span> <span class="o">=</span> <span class="n">format</span><span class="p">(</span><span class="n">optionals</span> <span class="o">+</span> <span class="n">positionals</span><span class="p">,</span> <span class="n">groups</span><span class="p">)</span></span><a href="#l319"></a>
<span id="l320">            <span class="n">usage</span> <span class="o">=</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">s</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="p">[</span><span class="n">prog</span><span class="p">,</span> <span class="n">action_usage</span><span class="p">]</span> <span class="k">if</span> <span class="n">s</span><span class="p">])</span></span><a href="#l320"></a>
<span id="l321"></span><a href="#l321"></a>
<span id="l322">            <span class="c"># wrap the usage parts if it&#39;s too long</span></span><a href="#l322"></a>
<span id="l323">            <span class="n">text_width</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_width</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_indent</span></span><a href="#l323"></a>
<span id="l324">            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">prefix</span><span class="p">)</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">usage</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">text_width</span><span class="p">:</span></span><a href="#l324"></a>
<span id="l325"></span><a href="#l325"></a>
<span id="l326">                <span class="c"># break usage into wrappable parts</span></span><a href="#l326"></a>
<span id="l327">                <span class="n">part_regexp</span> <span class="o">=</span> <span class="s">r&#39;\(.*?\)+|\[.*?\]+|\S+&#39;</span></span><a href="#l327"></a>
<span id="l328">                <span class="n">opt_usage</span> <span class="o">=</span> <span class="n">format</span><span class="p">(</span><span class="n">optionals</span><span class="p">,</span> <span class="n">groups</span><span class="p">)</span></span><a href="#l328"></a>
<span id="l329">                <span class="n">pos_usage</span> <span class="o">=</span> <span class="n">format</span><span class="p">(</span><span class="n">positionals</span><span class="p">,</span> <span class="n">groups</span><span class="p">)</span></span><a href="#l329"></a>
<span id="l330">                <span class="n">opt_parts</span> <span class="o">=</span> <span class="n">_re</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="n">part_regexp</span><span class="p">,</span> <span class="n">opt_usage</span><span class="p">)</span></span><a href="#l330"></a>
<span id="l331">                <span class="n">pos_parts</span> <span class="o">=</span> <span class="n">_re</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="n">part_regexp</span><span class="p">,</span> <span class="n">pos_usage</span><span class="p">)</span></span><a href="#l331"></a>
<span id="l332">                <span class="k">assert</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">opt_parts</span><span class="p">)</span> <span class="o">==</span> <span class="n">opt_usage</span></span><a href="#l332"></a>
<span id="l333">                <span class="k">assert</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">pos_parts</span><span class="p">)</span> <span class="o">==</span> <span class="n">pos_usage</span></span><a href="#l333"></a>
<span id="l334"></span><a href="#l334"></a>
<span id="l335">                <span class="c"># helper for wrapping lines</span></span><a href="#l335"></a>
<span id="l336">                <span class="k">def</span> <span class="nf">get_lines</span><span class="p">(</span><span class="n">parts</span><span class="p">,</span> <span class="n">indent</span><span class="p">,</span> <span class="n">prefix</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l336"></a>
<span id="l337">                    <span class="n">lines</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l337"></a>
<span id="l338">                    <span class="n">line</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l338"></a>
<span id="l339">                    <span class="k">if</span> <span class="n">prefix</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l339"></a>
<span id="l340">                        <span class="n">line_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">prefix</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span></span><a href="#l340"></a>
<span id="l341">                    <span class="k">else</span><span class="p">:</span></span><a href="#l341"></a>
<span id="l342">                        <span class="n">line_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">indent</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span></span><a href="#l342"></a>
<span id="l343">                    <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">parts</span><span class="p">:</span></span><a href="#l343"></a>
<span id="l344">                        <span class="k">if</span> <span class="n">line_len</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">part</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">text_width</span> <span class="ow">and</span> <span class="n">line</span><span class="p">:</span></span><a href="#l344"></a>
<span id="l345">                            <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">indent</span> <span class="o">+</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">line</span><span class="p">))</span></span><a href="#l345"></a>
<span id="l346">                            <span class="n">line</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l346"></a>
<span id="l347">                            <span class="n">line_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">indent</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span></span><a href="#l347"></a>
<span id="l348">                        <span class="n">line</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">part</span><span class="p">)</span></span><a href="#l348"></a>
<span id="l349">                        <span class="n">line_len</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="n">part</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span></span><a href="#l349"></a>
<span id="l350">                    <span class="k">if</span> <span class="n">line</span><span class="p">:</span></span><a href="#l350"></a>
<span id="l351">                        <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">indent</span> <span class="o">+</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">line</span><span class="p">))</span></span><a href="#l351"></a>
<span id="l352">                    <span class="k">if</span> <span class="n">prefix</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l352"></a>
<span id="l353">                        <span class="n">lines</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="n">lines</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="nb">len</span><span class="p">(</span><span class="n">indent</span><span class="p">):]</span></span><a href="#l353"></a>
<span id="l354">                    <span class="k">return</span> <span class="n">lines</span></span><a href="#l354"></a>
<span id="l355"></span><a href="#l355"></a>
<span id="l356">                <span class="c"># if prog is short, follow it with optionals or positionals</span></span><a href="#l356"></a>
<span id="l357">                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">prefix</span><span class="p">)</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">prog</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mf">0.75</span> <span class="o">*</span> <span class="n">text_width</span><span class="p">:</span></span><a href="#l357"></a>
<span id="l358">                    <span class="n">indent</span> <span class="o">=</span> <span class="s">&#39; &#39;</span> <span class="o">*</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">prefix</span><span class="p">)</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">prog</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span></span><a href="#l358"></a>
<span id="l359">                    <span class="k">if</span> <span class="n">opt_parts</span><span class="p">:</span></span><a href="#l359"></a>
<span id="l360">                        <span class="n">lines</span> <span class="o">=</span> <span class="n">get_lines</span><span class="p">([</span><span class="n">prog</span><span class="p">]</span> <span class="o">+</span> <span class="n">opt_parts</span><span class="p">,</span> <span class="n">indent</span><span class="p">,</span> <span class="n">prefix</span><span class="p">)</span></span><a href="#l360"></a>
<span id="l361">                        <span class="n">lines</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">get_lines</span><span class="p">(</span><span class="n">pos_parts</span><span class="p">,</span> <span class="n">indent</span><span class="p">))</span></span><a href="#l361"></a>
<span id="l362">                    <span class="k">elif</span> <span class="n">pos_parts</span><span class="p">:</span></span><a href="#l362"></a>
<span id="l363">                        <span class="n">lines</span> <span class="o">=</span> <span class="n">get_lines</span><span class="p">([</span><span class="n">prog</span><span class="p">]</span> <span class="o">+</span> <span class="n">pos_parts</span><span class="p">,</span> <span class="n">indent</span><span class="p">,</span> <span class="n">prefix</span><span class="p">)</span></span><a href="#l363"></a>
<span id="l364">                    <span class="k">else</span><span class="p">:</span></span><a href="#l364"></a>
<span id="l365">                        <span class="n">lines</span> <span class="o">=</span> <span class="p">[</span><span class="n">prog</span><span class="p">]</span></span><a href="#l365"></a>
<span id="l366"></span><a href="#l366"></a>
<span id="l367">                <span class="c"># if prog is long, put it on its own line</span></span><a href="#l367"></a>
<span id="l368">                <span class="k">else</span><span class="p">:</span></span><a href="#l368"></a>
<span id="l369">                    <span class="n">indent</span> <span class="o">=</span> <span class="s">&#39; &#39;</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="n">prefix</span><span class="p">)</span></span><a href="#l369"></a>
<span id="l370">                    <span class="n">parts</span> <span class="o">=</span> <span class="n">opt_parts</span> <span class="o">+</span> <span class="n">pos_parts</span></span><a href="#l370"></a>
<span id="l371">                    <span class="n">lines</span> <span class="o">=</span> <span class="n">get_lines</span><span class="p">(</span><span class="n">parts</span><span class="p">,</span> <span class="n">indent</span><span class="p">)</span></span><a href="#l371"></a>
<span id="l372">                    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">lines</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l372"></a>
<span id="l373">                        <span class="n">lines</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l373"></a>
<span id="l374">                        <span class="n">lines</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">get_lines</span><span class="p">(</span><span class="n">opt_parts</span><span class="p">,</span> <span class="n">indent</span><span class="p">))</span></span><a href="#l374"></a>
<span id="l375">                        <span class="n">lines</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">get_lines</span><span class="p">(</span><span class="n">pos_parts</span><span class="p">,</span> <span class="n">indent</span><span class="p">))</span></span><a href="#l375"></a>
<span id="l376">                    <span class="n">lines</span> <span class="o">=</span> <span class="p">[</span><span class="n">prog</span><span class="p">]</span> <span class="o">+</span> <span class="n">lines</span></span><a href="#l376"></a>
<span id="l377"></span><a href="#l377"></a>
<span id="l378">                <span class="c"># join lines into usage</span></span><a href="#l378"></a>
<span id="l379">                <span class="n">usage</span> <span class="o">=</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lines</span><span class="p">)</span></span><a href="#l379"></a>
<span id="l380"></span><a href="#l380"></a>
<span id="l381">        <span class="c"># prefix with &#39;usage:&#39;</span></span><a href="#l381"></a>
<span id="l382">        <span class="k">return</span> <span class="s">&#39;</span><span class="si">%s%s</span><span class="se">\n\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">usage</span><span class="p">)</span></span><a href="#l382"></a>
<span id="l383"></span><a href="#l383"></a>
<span id="l384">    <span class="k">def</span> <span class="nf">_format_actions_usage</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">actions</span><span class="p">,</span> <span class="n">groups</span><span class="p">):</span></span><a href="#l384"></a>
<span id="l385">        <span class="c"># find group indices and identify actions in groups</span></span><a href="#l385"></a>
<span id="l386">        <span class="n">group_actions</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span></span><a href="#l386"></a>
<span id="l387">        <span class="n">inserts</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l387"></a>
<span id="l388">        <span class="k">for</span> <span class="n">group</span> <span class="ow">in</span> <span class="n">groups</span><span class="p">:</span></span><a href="#l388"></a>
<span id="l389">            <span class="k">try</span><span class="p">:</span></span><a href="#l389"></a>
<span id="l390">                <span class="n">start</span> <span class="o">=</span> <span class="n">actions</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">group</span><span class="o">.</span><span class="n">_group_actions</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span></span><a href="#l390"></a>
<span id="l391">            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span></span><a href="#l391"></a>
<span id="l392">                <span class="k">continue</span></span><a href="#l392"></a>
<span id="l393">            <span class="k">else</span><span class="p">:</span></span><a href="#l393"></a>
<span id="l394">                <span class="n">end</span> <span class="o">=</span> <span class="n">start</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">group</span><span class="o">.</span><span class="n">_group_actions</span><span class="p">)</span></span><a href="#l394"></a>
<span id="l395">                <span class="k">if</span> <span class="n">actions</span><span class="p">[</span><span class="n">start</span><span class="p">:</span><span class="n">end</span><span class="p">]</span> <span class="o">==</span> <span class="n">group</span><span class="o">.</span><span class="n">_group_actions</span><span class="p">:</span></span><a href="#l395"></a>
<span id="l396">                    <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">group</span><span class="o">.</span><span class="n">_group_actions</span><span class="p">:</span></span><a href="#l396"></a>
<span id="l397">                        <span class="n">group_actions</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l397"></a>
<span id="l398">                    <span class="k">if</span> <span class="ow">not</span> <span class="n">group</span><span class="o">.</span><span class="n">required</span><span class="p">:</span></span><a href="#l398"></a>
<span id="l399">                        <span class="k">if</span> <span class="n">start</span> <span class="ow">in</span> <span class="n">inserts</span><span class="p">:</span></span><a href="#l399"></a>
<span id="l400">                            <span class="n">inserts</span><span class="p">[</span><span class="n">start</span><span class="p">]</span> <span class="o">+=</span> <span class="s">&#39; [&#39;</span></span><a href="#l400"></a>
<span id="l401">                        <span class="k">else</span><span class="p">:</span></span><a href="#l401"></a>
<span id="l402">                            <span class="n">inserts</span><span class="p">[</span><span class="n">start</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;[&#39;</span></span><a href="#l402"></a>
<span id="l403">                        <span class="n">inserts</span><span class="p">[</span><span class="n">end</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;]&#39;</span></span><a href="#l403"></a>
<span id="l404">                    <span class="k">else</span><span class="p">:</span></span><a href="#l404"></a>
<span id="l405">                        <span class="k">if</span> <span class="n">start</span> <span class="ow">in</span> <span class="n">inserts</span><span class="p">:</span></span><a href="#l405"></a>
<span id="l406">                            <span class="n">inserts</span><span class="p">[</span><span class="n">start</span><span class="p">]</span> <span class="o">+=</span> <span class="s">&#39; (&#39;</span></span><a href="#l406"></a>
<span id="l407">                        <span class="k">else</span><span class="p">:</span></span><a href="#l407"></a>
<span id="l408">                            <span class="n">inserts</span><span class="p">[</span><span class="n">start</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;(&#39;</span></span><a href="#l408"></a>
<span id="l409">                        <span class="n">inserts</span><span class="p">[</span><span class="n">end</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;)&#39;</span></span><a href="#l409"></a>
<span id="l410">                    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">start</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="n">end</span><span class="p">):</span></span><a href="#l410"></a>
<span id="l411">                        <span class="n">inserts</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;|&#39;</span></span><a href="#l411"></a>
<span id="l412"></span><a href="#l412"></a>
<span id="l413">        <span class="c"># collect all actions format strings</span></span><a href="#l413"></a>
<span id="l414">        <span class="n">parts</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l414"></a>
<span id="l415">        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">action</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">actions</span><span class="p">):</span></span><a href="#l415"></a>
<span id="l416"></span><a href="#l416"></a>
<span id="l417">            <span class="c"># suppressed arguments are marked with None</span></span><a href="#l417"></a>
<span id="l418">            <span class="c"># remove | separators for suppressed arguments</span></span><a href="#l418"></a>
<span id="l419">            <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">help</span> <span class="ow">is</span> <span class="n">SUPPRESS</span><span class="p">:</span></span><a href="#l419"></a>
<span id="l420">                <span class="n">parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">None</span><span class="p">)</span></span><a href="#l420"></a>
<span id="l421">                <span class="k">if</span> <span class="n">inserts</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="o">==</span> <span class="s">&#39;|&#39;</span><span class="p">:</span></span><a href="#l421"></a>
<span id="l422">                    <span class="n">inserts</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">i</span><span class="p">)</span></span><a href="#l422"></a>
<span id="l423">                <span class="k">elif</span> <span class="n">inserts</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="o">==</span> <span class="s">&#39;|&#39;</span><span class="p">:</span></span><a href="#l423"></a>
<span id="l424">                    <span class="n">inserts</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span></span><a href="#l424"></a>
<span id="l425"></span><a href="#l425"></a>
<span id="l426">            <span class="c"># produce all arg strings</span></span><a href="#l426"></a>
<span id="l427">            <span class="k">elif</span> <span class="ow">not</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">:</span></span><a href="#l427"></a>
<span id="l428">                <span class="n">part</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_args</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">dest</span><span class="p">)</span></span><a href="#l428"></a>
<span id="l429"></span><a href="#l429"></a>
<span id="l430">                <span class="c"># if it&#39;s in a group, strip the outer []</span></span><a href="#l430"></a>
<span id="l431">                <span class="k">if</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">group_actions</span><span class="p">:</span></span><a href="#l431"></a>
<span id="l432">                    <span class="k">if</span> <span class="n">part</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;[&#39;</span> <span class="ow">and</span> <span class="n">part</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;]&#39;</span><span class="p">:</span></span><a href="#l432"></a>
<span id="l433">                        <span class="n">part</span> <span class="o">=</span> <span class="n">part</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l433"></a>
<span id="l434"></span><a href="#l434"></a>
<span id="l435">                <span class="c"># add the action string to the list</span></span><a href="#l435"></a>
<span id="l436">                <span class="n">parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">part</span><span class="p">)</span></span><a href="#l436"></a>
<span id="l437"></span><a href="#l437"></a>
<span id="l438">            <span class="c"># produce the first way to invoke the option in brackets</span></span><a href="#l438"></a>
<span id="l439">            <span class="k">else</span><span class="p">:</span></span><a href="#l439"></a>
<span id="l440">                <span class="n">option_string</span> <span class="o">=</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l440"></a>
<span id="l441"></span><a href="#l441"></a>
<span id="l442">                <span class="c"># if the Optional doesn&#39;t take a value, format is:</span></span><a href="#l442"></a>
<span id="l443">                <span class="c">#    -s or --long</span></span><a href="#l443"></a>
<span id="l444">                <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l444"></a>
<span id="l445">                    <span class="n">part</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">option_string</span></span><a href="#l445"></a>
<span id="l446"></span><a href="#l446"></a>
<span id="l447">                <span class="c"># if the Optional takes a value, format is:</span></span><a href="#l447"></a>
<span id="l448">                <span class="c">#    -s ARGS or --long ARGS</span></span><a href="#l448"></a>
<span id="l449">                <span class="k">else</span><span class="p">:</span></span><a href="#l449"></a>
<span id="l450">                    <span class="n">default</span> <span class="o">=</span> <span class="n">action</span><span class="o">.</span><span class="n">dest</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span></span><a href="#l450"></a>
<span id="l451">                    <span class="n">args_string</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_args</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">default</span><span class="p">)</span></span><a href="#l451"></a>
<span id="l452">                    <span class="n">part</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s"> </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">option_string</span><span class="p">,</span> <span class="n">args_string</span><span class="p">)</span></span><a href="#l452"></a>
<span id="l453"></span><a href="#l453"></a>
<span id="l454">                <span class="c"># make it look optional if it&#39;s not required or in a group</span></span><a href="#l454"></a>
<span id="l455">                <span class="k">if</span> <span class="ow">not</span> <span class="n">action</span><span class="o">.</span><span class="n">required</span> <span class="ow">and</span> <span class="n">action</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">group_actions</span><span class="p">:</span></span><a href="#l455"></a>
<span id="l456">                    <span class="n">part</span> <span class="o">=</span> <span class="s">&#39;[</span><span class="si">%s</span><span class="s">]&#39;</span> <span class="o">%</span> <span class="n">part</span></span><a href="#l456"></a>
<span id="l457"></span><a href="#l457"></a>
<span id="l458">                <span class="c"># add the action string to the list</span></span><a href="#l458"></a>
<span id="l459">                <span class="n">parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">part</span><span class="p">)</span></span><a href="#l459"></a>
<span id="l460"></span><a href="#l460"></a>
<span id="l461">        <span class="c"># insert things at the necessary indices</span></span><a href="#l461"></a>
<span id="l462">        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">inserts</span><span class="p">,</span> <span class="n">reverse</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></span><a href="#l462"></a>
<span id="l463">            <span class="n">parts</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">inserts</span><span class="p">[</span><span class="n">i</span><span class="p">]]</span></span><a href="#l463"></a>
<span id="l464"></span><a href="#l464"></a>
<span id="l465">        <span class="c"># join all the action items with spaces</span></span><a href="#l465"></a>
<span id="l466">        <span class="n">text</span> <span class="o">=</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">item</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">parts</span> <span class="k">if</span> <span class="n">item</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">])</span></span><a href="#l466"></a>
<span id="l467"></span><a href="#l467"></a>
<span id="l468">        <span class="c"># clean up separators for mutually exclusive groups</span></span><a href="#l468"></a>
<span id="l469">        <span class="nb">open</span> <span class="o">=</span> <span class="s">r&#39;[\[(]&#39;</span></span><a href="#l469"></a>
<span id="l470">        <span class="n">close</span> <span class="o">=</span> <span class="s">r&#39;[\])]&#39;</span></span><a href="#l470"></a>
<span id="l471">        <span class="n">text</span> <span class="o">=</span> <span class="n">_re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">r&#39;(</span><span class="si">%s</span><span class="s">) &#39;</span> <span class="o">%</span> <span class="nb">open</span><span class="p">,</span> <span class="s">r&#39;\1&#39;</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span></span><a href="#l471"></a>
<span id="l472">        <span class="n">text</span> <span class="o">=</span> <span class="n">_re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">r&#39; (</span><span class="si">%s</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="n">close</span><span class="p">,</span> <span class="s">r&#39;\1&#39;</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span></span><a href="#l472"></a>
<span id="l473">        <span class="n">text</span> <span class="o">=</span> <span class="n">_re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">r&#39;</span><span class="si">%s</span><span class="s"> *</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="nb">open</span><span class="p">,</span> <span class="n">close</span><span class="p">),</span> <span class="s">r&#39;&#39;</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span></span><a href="#l473"></a>
<span id="l474">        <span class="n">text</span> <span class="o">=</span> <span class="n">_re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">r&#39;\(([^|]*)\)&#39;</span><span class="p">,</span> <span class="s">r&#39;\1&#39;</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span></span><a href="#l474"></a>
<span id="l475">        <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></span><a href="#l475"></a>
<span id="l476"></span><a href="#l476"></a>
<span id="l477">        <span class="c"># return the text</span></span><a href="#l477"></a>
<span id="l478">        <span class="k">return</span> <span class="n">text</span></span><a href="#l478"></a>
<span id="l479"></span><a href="#l479"></a>
<span id="l480">    <span class="k">def</span> <span class="nf">_format_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">):</span></span><a href="#l480"></a>
<span id="l481">        <span class="k">if</span> <span class="s">&#39;%(prog)&#39;</span> <span class="ow">in</span> <span class="n">text</span><span class="p">:</span></span><a href="#l481"></a>
<span id="l482">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span> <span class="o">%</span> <span class="nb">dict</span><span class="p">(</span><span class="n">prog</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_prog</span><span class="p">)</span></span><a href="#l482"></a>
<span id="l483">        <span class="n">text_width</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_width</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_indent</span><span class="p">,</span> <span class="mi">11</span><span class="p">)</span></span><a href="#l483"></a>
<span id="l484">        <span class="n">indent</span> <span class="o">=</span> <span class="s">&#39; &#39;</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_indent</span></span><a href="#l484"></a>
<span id="l485">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fill_text</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">text_width</span><span class="p">,</span> <span class="n">indent</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n\n</span><span class="s">&#39;</span></span><a href="#l485"></a>
<span id="l486"></span><a href="#l486"></a>
<span id="l487">    <span class="k">def</span> <span class="nf">_format_action</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l487"></a>
<span id="l488">        <span class="c"># determine the required width and the entry label</span></span><a href="#l488"></a>
<span id="l489">        <span class="n">help_position</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_action_max_length</span> <span class="o">+</span> <span class="mi">2</span><span class="p">,</span></span><a href="#l489"></a>
<span id="l490">                            <span class="bp">self</span><span class="o">.</span><span class="n">_max_help_position</span><span class="p">)</span></span><a href="#l490"></a>
<span id="l491">        <span class="n">help_width</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_width</span> <span class="o">-</span> <span class="n">help_position</span><span class="p">,</span> <span class="mi">11</span><span class="p">)</span></span><a href="#l491"></a>
<span id="l492">        <span class="n">action_width</span> <span class="o">=</span> <span class="n">help_position</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_indent</span> <span class="o">-</span> <span class="mi">2</span></span><a href="#l492"></a>
<span id="l493">        <span class="n">action_header</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_action_invocation</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l493"></a>
<span id="l494"></span><a href="#l494"></a>
<span id="l495">        <span class="c"># ho nelp; start on same line and add a final newline</span></span><a href="#l495"></a>
<span id="l496">        <span class="k">if</span> <span class="ow">not</span> <span class="n">action</span><span class="o">.</span><span class="n">help</span><span class="p">:</span></span><a href="#l496"></a>
<span id="l497">            <span class="n">tup</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_indent</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">action_header</span></span><a href="#l497"></a>
<span id="l498">            <span class="n">action_header</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%*s%s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">tup</span></span><a href="#l498"></a>
<span id="l499"></span><a href="#l499"></a>
<span id="l500">        <span class="c"># short action name; start on the same line and pad two spaces</span></span><a href="#l500"></a>
<span id="l501">        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">action_header</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="n">action_width</span><span class="p">:</span></span><a href="#l501"></a>
<span id="l502">            <span class="n">tup</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_indent</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">action_width</span><span class="p">,</span> <span class="n">action_header</span></span><a href="#l502"></a>
<span id="l503">            <span class="n">action_header</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%*s%-*s</span><span class="s">  &#39;</span> <span class="o">%</span> <span class="n">tup</span></span><a href="#l503"></a>
<span id="l504">            <span class="n">indent_first</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l504"></a>
<span id="l505"></span><a href="#l505"></a>
<span id="l506">        <span class="c"># long action name; start on the next line</span></span><a href="#l506"></a>
<span id="l507">        <span class="k">else</span><span class="p">:</span></span><a href="#l507"></a>
<span id="l508">            <span class="n">tup</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_indent</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">action_header</span></span><a href="#l508"></a>
<span id="l509">            <span class="n">action_header</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%*s%s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">tup</span></span><a href="#l509"></a>
<span id="l510">            <span class="n">indent_first</span> <span class="o">=</span> <span class="n">help_position</span></span><a href="#l510"></a>
<span id="l511"></span><a href="#l511"></a>
<span id="l512">        <span class="c"># collect the pieces of the action help</span></span><a href="#l512"></a>
<span id="l513">        <span class="n">parts</span> <span class="o">=</span> <span class="p">[</span><span class="n">action_header</span><span class="p">]</span></span><a href="#l513"></a>
<span id="l514"></span><a href="#l514"></a>
<span id="l515">        <span class="c"># if there was help for the action, add lines of help text</span></span><a href="#l515"></a>
<span id="l516">        <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">help</span><span class="p">:</span></span><a href="#l516"></a>
<span id="l517">            <span class="n">help_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_expand_help</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l517"></a>
<span id="l518">            <span class="n">help_lines</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_split_lines</span><span class="p">(</span><span class="n">help_text</span><span class="p">,</span> <span class="n">help_width</span><span class="p">)</span></span><a href="#l518"></a>
<span id="l519">            <span class="n">parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%*s%s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">indent_first</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">help_lines</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span></span><a href="#l519"></a>
<span id="l520">            <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">help_lines</span><span class="p">[</span><span class="mi">1</span><span class="p">:]:</span></span><a href="#l520"></a>
<span id="l521">                <span class="n">parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%*s%s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">help_position</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">line</span><span class="p">))</span></span><a href="#l521"></a>
<span id="l522"></span><a href="#l522"></a>
<span id="l523">        <span class="c"># or add a newline if the description doesn&#39;t end with one</span></span><a href="#l523"></a>
<span id="l524">        <span class="k">elif</span> <span class="ow">not</span> <span class="n">action_header</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">):</span></span><a href="#l524"></a>
<span id="l525">            <span class="n">parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l525"></a>
<span id="l526"></span><a href="#l526"></a>
<span id="l527">        <span class="c"># if there are any sub-actions, add their help as well</span></span><a href="#l527"></a>
<span id="l528">        <span class="k">for</span> <span class="n">subaction</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_iter_indented_subactions</span><span class="p">(</span><span class="n">action</span><span class="p">):</span></span><a href="#l528"></a>
<span id="l529">            <span class="n">parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_format_action</span><span class="p">(</span><span class="n">subaction</span><span class="p">))</span></span><a href="#l529"></a>
<span id="l530"></span><a href="#l530"></a>
<span id="l531">        <span class="c"># return a single string</span></span><a href="#l531"></a>
<span id="l532">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_join_parts</span><span class="p">(</span><span class="n">parts</span><span class="p">)</span></span><a href="#l532"></a>
<span id="l533"></span><a href="#l533"></a>
<span id="l534">    <span class="k">def</span> <span class="nf">_format_action_invocation</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l534"></a>
<span id="l535">        <span class="k">if</span> <span class="ow">not</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">:</span></span><a href="#l535"></a>
<span id="l536">            <span class="n">metavar</span><span class="p">,</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metavar_formatter</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">dest</span><span class="p">)(</span><span class="mi">1</span><span class="p">)</span></span><a href="#l536"></a>
<span id="l537">            <span class="k">return</span> <span class="n">metavar</span></span><a href="#l537"></a>
<span id="l538"></span><a href="#l538"></a>
<span id="l539">        <span class="k">else</span><span class="p">:</span></span><a href="#l539"></a>
<span id="l540">            <span class="n">parts</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l540"></a>
<span id="l541"></span><a href="#l541"></a>
<span id="l542">            <span class="c"># if the Optional doesn&#39;t take a value, format is:</span></span><a href="#l542"></a>
<span id="l543">            <span class="c">#    -s, --long</span></span><a href="#l543"></a>
<span id="l544">            <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l544"></a>
<span id="l545">                <span class="n">parts</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">)</span></span><a href="#l545"></a>
<span id="l546"></span><a href="#l546"></a>
<span id="l547">            <span class="c"># if the Optional takes a value, format is:</span></span><a href="#l547"></a>
<span id="l548">            <span class="c">#    -s ARGS, --long ARGS</span></span><a href="#l548"></a>
<span id="l549">            <span class="k">else</span><span class="p">:</span></span><a href="#l549"></a>
<span id="l550">                <span class="n">default</span> <span class="o">=</span> <span class="n">action</span><span class="o">.</span><span class="n">dest</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span></span><a href="#l550"></a>
<span id="l551">                <span class="n">args_string</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_args</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">default</span><span class="p">)</span></span><a href="#l551"></a>
<span id="l552">                <span class="k">for</span> <span class="n">option_string</span> <span class="ow">in</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">:</span></span><a href="#l552"></a>
<span id="l553">                    <span class="n">parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s"> </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">option_string</span><span class="p">,</span> <span class="n">args_string</span><span class="p">))</span></span><a href="#l553"></a>
<span id="l554"></span><a href="#l554"></a>
<span id="l555">            <span class="k">return</span> <span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">parts</span><span class="p">)</span></span><a href="#l555"></a>
<span id="l556"></span><a href="#l556"></a>
<span id="l557">    <span class="k">def</span> <span class="nf">_metavar_formatter</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">default_metavar</span><span class="p">):</span></span><a href="#l557"></a>
<span id="l558">        <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">metavar</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l558"></a>
<span id="l559">            <span class="n">result</span> <span class="o">=</span> <span class="n">action</span><span class="o">.</span><span class="n">metavar</span></span><a href="#l559"></a>
<span id="l560">        <span class="k">elif</span> <span class="n">action</span><span class="o">.</span><span class="n">choices</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l560"></a>
<span id="l561">            <span class="n">choice_strs</span> <span class="o">=</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">choice</span><span class="p">)</span> <span class="k">for</span> <span class="n">choice</span> <span class="ow">in</span> <span class="n">action</span><span class="o">.</span><span class="n">choices</span><span class="p">]</span></span><a href="#l561"></a>
<span id="l562">            <span class="n">result</span> <span class="o">=</span> <span class="s">&#39;{</span><span class="si">%s</span><span class="s">}&#39;</span> <span class="o">%</span> <span class="s">&#39;,&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">choice_strs</span><span class="p">)</span></span><a href="#l562"></a>
<span id="l563">        <span class="k">else</span><span class="p">:</span></span><a href="#l563"></a>
<span id="l564">            <span class="n">result</span> <span class="o">=</span> <span class="n">default_metavar</span></span><a href="#l564"></a>
<span id="l565"></span><a href="#l565"></a>
<span id="l566">        <span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="n">tuple_size</span><span class="p">):</span></span><a href="#l566"></a>
<span id="l567">            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span></span><a href="#l567"></a>
<span id="l568">                <span class="k">return</span> <span class="n">result</span></span><a href="#l568"></a>
<span id="l569">            <span class="k">else</span><span class="p">:</span></span><a href="#l569"></a>
<span id="l570">                <span class="k">return</span> <span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="p">)</span> <span class="o">*</span> <span class="n">tuple_size</span></span><a href="#l570"></a>
<span id="l571">        <span class="k">return</span> <span class="n">format</span></span><a href="#l571"></a>
<span id="l572"></span><a href="#l572"></a>
<span id="l573">    <span class="k">def</span> <span class="nf">_format_args</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">default_metavar</span><span class="p">):</span></span><a href="#l573"></a>
<span id="l574">        <span class="n">get_metavar</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metavar_formatter</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">default_metavar</span><span class="p">)</span></span><a href="#l574"></a>
<span id="l575">        <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l575"></a>
<span id="l576">            <span class="n">result</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">get_metavar</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span></span><a href="#l576"></a>
<span id="l577">        <span class="k">elif</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="o">==</span> <span class="n">OPTIONAL</span><span class="p">:</span></span><a href="#l577"></a>
<span id="l578">            <span class="n">result</span> <span class="o">=</span> <span class="s">&#39;[</span><span class="si">%s</span><span class="s">]&#39;</span> <span class="o">%</span> <span class="n">get_metavar</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span></span><a href="#l578"></a>
<span id="l579">        <span class="k">elif</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="o">==</span> <span class="n">ZERO_OR_MORE</span><span class="p">:</span></span><a href="#l579"></a>
<span id="l580">            <span class="n">result</span> <span class="o">=</span> <span class="s">&#39;[</span><span class="si">%s</span><span class="s"> [</span><span class="si">%s</span><span class="s"> ...]]&#39;</span> <span class="o">%</span> <span class="n">get_metavar</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span></span><a href="#l580"></a>
<span id="l581">        <span class="k">elif</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="o">==</span> <span class="n">ONE_OR_MORE</span><span class="p">:</span></span><a href="#l581"></a>
<span id="l582">            <span class="n">result</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s"> [</span><span class="si">%s</span><span class="s"> ...]&#39;</span> <span class="o">%</span> <span class="n">get_metavar</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span></span><a href="#l582"></a>
<span id="l583">        <span class="k">elif</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="o">==</span> <span class="n">REMAINDER</span><span class="p">:</span></span><a href="#l583"></a>
<span id="l584">            <span class="n">result</span> <span class="o">=</span> <span class="s">&#39;...&#39;</span></span><a href="#l584"></a>
<span id="l585">        <span class="k">elif</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="o">==</span> <span class="n">PARSER</span><span class="p">:</span></span><a href="#l585"></a>
<span id="l586">            <span class="n">result</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s"> ...&#39;</span> <span class="o">%</span> <span class="n">get_metavar</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span></span><a href="#l586"></a>
<span id="l587">        <span class="k">else</span><span class="p">:</span></span><a href="#l587"></a>
<span id="l588">            <span class="n">formats</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;</span><span class="si">%s</span><span class="s">&#39;</span> <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">action</span><span class="o">.</span><span class="n">nargs</span><span class="p">)]</span></span><a href="#l588"></a>
<span id="l589">            <span class="n">result</span> <span class="o">=</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formats</span><span class="p">)</span> <span class="o">%</span> <span class="n">get_metavar</span><span class="p">(</span><span class="n">action</span><span class="o">.</span><span class="n">nargs</span><span class="p">)</span></span><a href="#l589"></a>
<span id="l590">        <span class="k">return</span> <span class="n">result</span></span><a href="#l590"></a>
<span id="l591"></span><a href="#l591"></a>
<span id="l592">    <span class="k">def</span> <span class="nf">_expand_help</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l592"></a>
<span id="l593">        <span class="n">params</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="nb">vars</span><span class="p">(</span><span class="n">action</span><span class="p">),</span> <span class="n">prog</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_prog</span><span class="p">)</span></span><a href="#l593"></a>
<span id="l594">        <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="nb">list</span><span class="p">(</span><span class="n">params</span><span class="p">):</span></span><a href="#l594"></a>
<span id="l595">            <span class="k">if</span> <span class="n">params</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="ow">is</span> <span class="n">SUPPRESS</span><span class="p">:</span></span><a href="#l595"></a>
<span id="l596">                <span class="k">del</span> <span class="n">params</span><span class="p">[</span><span class="n">name</span><span class="p">]</span></span><a href="#l596"></a>
<span id="l597">        <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="nb">list</span><span class="p">(</span><span class="n">params</span><span class="p">):</span></span><a href="#l597"></a>
<span id="l598">            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">params</span><span class="p">[</span><span class="n">name</span><span class="p">],</span> <span class="s">&#39;__name__&#39;</span><span class="p">):</span></span><a href="#l598"></a>
<span id="l599">                <span class="n">params</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">params</span><span class="p">[</span><span class="n">name</span><span class="p">]</span><span class="o">.</span><span class="n">__name__</span></span><a href="#l599"></a>
<span id="l600">        <span class="k">if</span> <span class="n">params</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;choices&#39;</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l600"></a>
<span id="l601">            <span class="n">choices_str</span> <span class="o">=</span> <span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">c</span><span class="p">)</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">params</span><span class="p">[</span><span class="s">&#39;choices&#39;</span><span class="p">]])</span></span><a href="#l601"></a>
<span id="l602">            <span class="n">params</span><span class="p">[</span><span class="s">&#39;choices&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">choices_str</span></span><a href="#l602"></a>
<span id="l603">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_help_string</span><span class="p">(</span><span class="n">action</span><span class="p">)</span> <span class="o">%</span> <span class="n">params</span></span><a href="#l603"></a>
<span id="l604"></span><a href="#l604"></a>
<span id="l605">    <span class="k">def</span> <span class="nf">_iter_indented_subactions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l605"></a>
<span id="l606">        <span class="k">try</span><span class="p">:</span></span><a href="#l606"></a>
<span id="l607">            <span class="n">get_subactions</span> <span class="o">=</span> <span class="n">action</span><span class="o">.</span><span class="n">_get_subactions</span></span><a href="#l607"></a>
<span id="l608">        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></span><a href="#l608"></a>
<span id="l609">            <span class="k">pass</span></span><a href="#l609"></a>
<span id="l610">        <span class="k">else</span><span class="p">:</span></span><a href="#l610"></a>
<span id="l611">            <span class="bp">self</span><span class="o">.</span><span class="n">_indent</span><span class="p">()</span></span><a href="#l611"></a>
<span id="l612">            <span class="k">for</span> <span class="n">subaction</span> <span class="ow">in</span> <span class="n">get_subactions</span><span class="p">():</span></span><a href="#l612"></a>
<span id="l613">                <span class="k">yield</span> <span class="n">subaction</span></span><a href="#l613"></a>
<span id="l614">            <span class="bp">self</span><span class="o">.</span><span class="n">_dedent</span><span class="p">()</span></span><a href="#l614"></a>
<span id="l615"></span><a href="#l615"></a>
<span id="l616">    <span class="k">def</span> <span class="nf">_split_lines</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">width</span><span class="p">):</span></span><a href="#l616"></a>
<span id="l617">        <span class="n">text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_whitespace_matcher</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></span><a href="#l617"></a>
<span id="l618">        <span class="k">return</span> <span class="n">_textwrap</span><span class="o">.</span><span class="n">wrap</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">width</span><span class="p">)</span></span><a href="#l618"></a>
<span id="l619"></span><a href="#l619"></a>
<span id="l620">    <span class="k">def</span> <span class="nf">_fill_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">indent</span><span class="p">):</span></span><a href="#l620"></a>
<span id="l621">        <span class="n">text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_whitespace_matcher</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></span><a href="#l621"></a>
<span id="l622">        <span class="k">return</span> <span class="n">_textwrap</span><span class="o">.</span><span class="n">fill</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">initial_indent</span><span class="o">=</span><span class="n">indent</span><span class="p">,</span></span><a href="#l622"></a>
<span id="l623">                                           <span class="n">subsequent_indent</span><span class="o">=</span><span class="n">indent</span><span class="p">)</span></span><a href="#l623"></a>
<span id="l624"></span><a href="#l624"></a>
<span id="l625">    <span class="k">def</span> <span class="nf">_get_help_string</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l625"></a>
<span id="l626">        <span class="k">return</span> <span class="n">action</span><span class="o">.</span><span class="n">help</span></span><a href="#l626"></a>
<span id="l627"></span><a href="#l627"></a>
<span id="l628"></span><a href="#l628"></a>
<span id="l629"><span class="k">class</span> <span class="nc">RawDescriptionHelpFormatter</span><span class="p">(</span><span class="n">HelpFormatter</span><span class="p">):</span></span><a href="#l629"></a>
<span id="l630">    <span class="sd">&quot;&quot;&quot;Help message formatter which retains any formatting in descriptions.</span></span><a href="#l630"></a>
<span id="l631"></span><a href="#l631"></a>
<span id="l632"><span class="sd">    Only the name of this class is considered a public API. All the methods</span></span><a href="#l632"></a>
<span id="l633"><span class="sd">    provided by the class are considered an implementation detail.</span></span><a href="#l633"></a>
<span id="l634"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l634"></a>
<span id="l635"></span><a href="#l635"></a>
<span id="l636">    <span class="k">def</span> <span class="nf">_fill_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">indent</span><span class="p">):</span></span><a href="#l636"></a>
<span id="l637">        <span class="k">return</span> <span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">indent</span> <span class="o">+</span> <span class="n">line</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">text</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(</span><span class="bp">True</span><span class="p">)])</span></span><a href="#l637"></a>
<span id="l638"></span><a href="#l638"></a>
<span id="l639"></span><a href="#l639"></a>
<span id="l640"><span class="k">class</span> <span class="nc">RawTextHelpFormatter</span><span class="p">(</span><span class="n">RawDescriptionHelpFormatter</span><span class="p">):</span></span><a href="#l640"></a>
<span id="l641">    <span class="sd">&quot;&quot;&quot;Help message formatter which retains formatting of all help text.</span></span><a href="#l641"></a>
<span id="l642"></span><a href="#l642"></a>
<span id="l643"><span class="sd">    Only the name of this class is considered a public API. All the methods</span></span><a href="#l643"></a>
<span id="l644"><span class="sd">    provided by the class are considered an implementation detail.</span></span><a href="#l644"></a>
<span id="l645"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l645"></a>
<span id="l646"></span><a href="#l646"></a>
<span id="l647">    <span class="k">def</span> <span class="nf">_split_lines</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">width</span><span class="p">):</span></span><a href="#l647"></a>
<span id="l648">        <span class="k">return</span> <span class="n">text</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()</span></span><a href="#l648"></a>
<span id="l649"></span><a href="#l649"></a>
<span id="l650"></span><a href="#l650"></a>
<span id="l651"><span class="k">class</span> <span class="nc">ArgumentDefaultsHelpFormatter</span><span class="p">(</span><span class="n">HelpFormatter</span><span class="p">):</span></span><a href="#l651"></a>
<span id="l652">    <span class="sd">&quot;&quot;&quot;Help message formatter which adds default values to argument help.</span></span><a href="#l652"></a>
<span id="l653"></span><a href="#l653"></a>
<span id="l654"><span class="sd">    Only the name of this class is considered a public API. All the methods</span></span><a href="#l654"></a>
<span id="l655"><span class="sd">    provided by the class are considered an implementation detail.</span></span><a href="#l655"></a>
<span id="l656"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l656"></a>
<span id="l657"></span><a href="#l657"></a>
<span id="l658">    <span class="k">def</span> <span class="nf">_get_help_string</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l658"></a>
<span id="l659">        <span class="n">help</span> <span class="o">=</span> <span class="n">action</span><span class="o">.</span><span class="n">help</span></span><a href="#l659"></a>
<span id="l660">        <span class="k">if</span> <span class="s">&#39;%(default)&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">action</span><span class="o">.</span><span class="n">help</span><span class="p">:</span></span><a href="#l660"></a>
<span id="l661">            <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">default</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">SUPPRESS</span><span class="p">:</span></span><a href="#l661"></a>
<span id="l662">                <span class="n">defaulting_nargs</span> <span class="o">=</span> <span class="p">[</span><span class="n">OPTIONAL</span><span class="p">,</span> <span class="n">ZERO_OR_MORE</span><span class="p">]</span></span><a href="#l662"></a>
<span id="l663">                <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span> <span class="ow">or</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="ow">in</span> <span class="n">defaulting_nargs</span><span class="p">:</span></span><a href="#l663"></a>
<span id="l664">                    <span class="n">help</span> <span class="o">+=</span> <span class="s">&#39; (default: </span><span class="si">%(default)s</span><span class="s">)&#39;</span></span><a href="#l664"></a>
<span id="l665">        <span class="k">return</span> <span class="n">help</span></span><a href="#l665"></a>
<span id="l666"></span><a href="#l666"></a>
<span id="l667"></span><a href="#l667"></a>
<span id="l668"><span class="c"># =====================</span></span><a href="#l668"></a>
<span id="l669"><span class="c"># Options and Arguments</span></span><a href="#l669"></a>
<span id="l670"><span class="c"># =====================</span></span><a href="#l670"></a>
<span id="l671"></span><a href="#l671"></a>
<span id="l672"><span class="k">def</span> <span class="nf">_get_action_name</span><span class="p">(</span><span class="n">argument</span><span class="p">):</span></span><a href="#l672"></a>
<span id="l673">    <span class="k">if</span> <span class="n">argument</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l673"></a>
<span id="l674">        <span class="k">return</span> <span class="bp">None</span></span><a href="#l674"></a>
<span id="l675">    <span class="k">elif</span> <span class="n">argument</span><span class="o">.</span><span class="n">option_strings</span><span class="p">:</span></span><a href="#l675"></a>
<span id="l676">        <span class="k">return</span>  <span class="s">&#39;/&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">argument</span><span class="o">.</span><span class="n">option_strings</span><span class="p">)</span></span><a href="#l676"></a>
<span id="l677">    <span class="k">elif</span> <span class="n">argument</span><span class="o">.</span><span class="n">metavar</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="n">SUPPRESS</span><span class="p">):</span></span><a href="#l677"></a>
<span id="l678">        <span class="k">return</span> <span class="n">argument</span><span class="o">.</span><span class="n">metavar</span></span><a href="#l678"></a>
<span id="l679">    <span class="k">elif</span> <span class="n">argument</span><span class="o">.</span><span class="n">dest</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="n">SUPPRESS</span><span class="p">):</span></span><a href="#l679"></a>
<span id="l680">        <span class="k">return</span> <span class="n">argument</span><span class="o">.</span><span class="n">dest</span></span><a href="#l680"></a>
<span id="l681">    <span class="k">else</span><span class="p">:</span></span><a href="#l681"></a>
<span id="l682">        <span class="k">return</span> <span class="bp">None</span></span><a href="#l682"></a>
<span id="l683"></span><a href="#l683"></a>
<span id="l684"></span><a href="#l684"></a>
<span id="l685"><span class="k">class</span> <span class="nc">ArgumentError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span></span><a href="#l685"></a>
<span id="l686">    <span class="sd">&quot;&quot;&quot;An error from creating or using an argument (optional or positional).</span></span><a href="#l686"></a>
<span id="l687"></span><a href="#l687"></a>
<span id="l688"><span class="sd">    The string value of this exception is the message, augmented with</span></span><a href="#l688"></a>
<span id="l689"><span class="sd">    information about the argument that caused it.</span></span><a href="#l689"></a>
<span id="l690"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l690"></a>
<span id="l691"></span><a href="#l691"></a>
<span id="l692">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">argument</span><span class="p">,</span> <span class="n">message</span><span class="p">):</span></span><a href="#l692"></a>
<span id="l693">        <span class="bp">self</span><span class="o">.</span><span class="n">argument_name</span> <span class="o">=</span> <span class="n">_get_action_name</span><span class="p">(</span><span class="n">argument</span><span class="p">)</span></span><a href="#l693"></a>
<span id="l694">        <span class="bp">self</span><span class="o">.</span><span class="n">message</span> <span class="o">=</span> <span class="n">message</span></span><a href="#l694"></a>
<span id="l695"></span><a href="#l695"></a>
<span id="l696">    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l696"></a>
<span id="l697">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">argument_name</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l697"></a>
<span id="l698">            <span class="n">format</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%(message)s</span><span class="s">&#39;</span></span><a href="#l698"></a>
<span id="l699">        <span class="k">else</span><span class="p">:</span></span><a href="#l699"></a>
<span id="l700">            <span class="n">format</span> <span class="o">=</span> <span class="s">&#39;argument </span><span class="si">%(argument_name)s</span><span class="s">: </span><span class="si">%(message)s</span><span class="s">&#39;</span></span><a href="#l700"></a>
<span id="l701">        <span class="k">return</span> <span class="n">format</span> <span class="o">%</span> <span class="nb">dict</span><span class="p">(</span><span class="n">message</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">message</span><span class="p">,</span></span><a href="#l701"></a>
<span id="l702">                             <span class="n">argument_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">argument_name</span><span class="p">)</span></span><a href="#l702"></a>
<span id="l703"></span><a href="#l703"></a>
<span id="l704"></span><a href="#l704"></a>
<span id="l705"><span class="k">class</span> <span class="nc">ArgumentTypeError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span></span><a href="#l705"></a>
<span id="l706">    <span class="sd">&quot;&quot;&quot;An error from trying to convert a command line string to a type.&quot;&quot;&quot;</span></span><a href="#l706"></a>
<span id="l707">    <span class="k">pass</span></span><a href="#l707"></a>
<span id="l708"></span><a href="#l708"></a>
<span id="l709"></span><a href="#l709"></a>
<span id="l710"><span class="c"># ==============</span></span><a href="#l710"></a>
<span id="l711"><span class="c"># Action classes</span></span><a href="#l711"></a>
<span id="l712"><span class="c"># ==============</span></span><a href="#l712"></a>
<span id="l713"></span><a href="#l713"></a>
<span id="l714"><span class="k">class</span> <span class="nc">Action</span><span class="p">(</span><span class="n">_AttributeHolder</span><span class="p">):</span></span><a href="#l714"></a>
<span id="l715">    <span class="sd">&quot;&quot;&quot;Information about how to convert command line strings to Python objects.</span></span><a href="#l715"></a>
<span id="l716"></span><a href="#l716"></a>
<span id="l717"><span class="sd">    Action objects are used by an ArgumentParser to represent the information</span></span><a href="#l717"></a>
<span id="l718"><span class="sd">    needed to parse a single argument from one or more strings from the</span></span><a href="#l718"></a>
<span id="l719"><span class="sd">    command line. The keyword arguments to the Action constructor are also</span></span><a href="#l719"></a>
<span id="l720"><span class="sd">    all attributes of Action instances.</span></span><a href="#l720"></a>
<span id="l721"></span><a href="#l721"></a>
<span id="l722"><span class="sd">    Keyword Arguments:</span></span><a href="#l722"></a>
<span id="l723"></span><a href="#l723"></a>
<span id="l724"><span class="sd">        - option_strings -- A list of command-line option strings which</span></span><a href="#l724"></a>
<span id="l725"><span class="sd">            should be associated with this action.</span></span><a href="#l725"></a>
<span id="l726"></span><a href="#l726"></a>
<span id="l727"><span class="sd">        - dest -- The name of the attribute to hold the created object(s)</span></span><a href="#l727"></a>
<span id="l728"></span><a href="#l728"></a>
<span id="l729"><span class="sd">        - nargs -- The number of command-line arguments that should be</span></span><a href="#l729"></a>
<span id="l730"><span class="sd">            consumed. By default, one argument will be consumed and a single</span></span><a href="#l730"></a>
<span id="l731"><span class="sd">            value will be produced.  Other values include:</span></span><a href="#l731"></a>
<span id="l732"><span class="sd">                - N (an integer) consumes N arguments (and produces a list)</span></span><a href="#l732"></a>
<span id="l733"><span class="sd">                - &#39;?&#39; consumes zero or one arguments</span></span><a href="#l733"></a>
<span id="l734"><span class="sd">                - &#39;*&#39; consumes zero or more arguments (and produces a list)</span></span><a href="#l734"></a>
<span id="l735"><span class="sd">                - &#39;+&#39; consumes one or more arguments (and produces a list)</span></span><a href="#l735"></a>
<span id="l736"><span class="sd">            Note that the difference between the default and nargs=1 is that</span></span><a href="#l736"></a>
<span id="l737"><span class="sd">            with the default, a single value will be produced, while with</span></span><a href="#l737"></a>
<span id="l738"><span class="sd">            nargs=1, a list containing a single value will be produced.</span></span><a href="#l738"></a>
<span id="l739"></span><a href="#l739"></a>
<span id="l740"><span class="sd">        - const -- The value to be produced if the option is specified and the</span></span><a href="#l740"></a>
<span id="l741"><span class="sd">            option uses an action that takes no values.</span></span><a href="#l741"></a>
<span id="l742"></span><a href="#l742"></a>
<span id="l743"><span class="sd">        - default -- The value to be produced if the option is not specified.</span></span><a href="#l743"></a>
<span id="l744"></span><a href="#l744"></a>
<span id="l745"><span class="sd">        - type -- A callable that accepts a single string argument, and</span></span><a href="#l745"></a>
<span id="l746"><span class="sd">            returns the converted value.  The standard Python types str, int,</span></span><a href="#l746"></a>
<span id="l747"><span class="sd">            float, and complex are useful examples of such callables.  If None,</span></span><a href="#l747"></a>
<span id="l748"><span class="sd">            str is used.</span></span><a href="#l748"></a>
<span id="l749"></span><a href="#l749"></a>
<span id="l750"><span class="sd">        - choices -- A container of values that should be allowed. If not None,</span></span><a href="#l750"></a>
<span id="l751"><span class="sd">            after a command-line argument has been converted to the appropriate</span></span><a href="#l751"></a>
<span id="l752"><span class="sd">            type, an exception will be raised if it is not a member of this</span></span><a href="#l752"></a>
<span id="l753"><span class="sd">            collection.</span></span><a href="#l753"></a>
<span id="l754"></span><a href="#l754"></a>
<span id="l755"><span class="sd">        - required -- True if the action must always be specified at the</span></span><a href="#l755"></a>
<span id="l756"><span class="sd">            command line. This is only meaningful for optional command-line</span></span><a href="#l756"></a>
<span id="l757"><span class="sd">            arguments.</span></span><a href="#l757"></a>
<span id="l758"></span><a href="#l758"></a>
<span id="l759"><span class="sd">        - help -- The help string describing the argument.</span></span><a href="#l759"></a>
<span id="l760"></span><a href="#l760"></a>
<span id="l761"><span class="sd">        - metavar -- The name to be used for the option&#39;s argument with the</span></span><a href="#l761"></a>
<span id="l762"><span class="sd">            help string. If None, the &#39;dest&#39; value will be used as the name.</span></span><a href="#l762"></a>
<span id="l763"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l763"></a>
<span id="l764"></span><a href="#l764"></a>
<span id="l765">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l765"></a>
<span id="l766">                 <span class="n">option_strings</span><span class="p">,</span></span><a href="#l766"></a>
<span id="l767">                 <span class="n">dest</span><span class="p">,</span></span><a href="#l767"></a>
<span id="l768">                 <span class="n">nargs</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l768"></a>
<span id="l769">                 <span class="n">const</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l769"></a>
<span id="l770">                 <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l770"></a>
<span id="l771">                 <span class="nb">type</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l771"></a>
<span id="l772">                 <span class="n">choices</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l772"></a>
<span id="l773">                 <span class="n">required</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></span><a href="#l773"></a>
<span id="l774">                 <span class="n">help</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l774"></a>
<span id="l775">                 <span class="n">metavar</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l775"></a>
<span id="l776">        <span class="bp">self</span><span class="o">.</span><span class="n">option_strings</span> <span class="o">=</span> <span class="n">option_strings</span></span><a href="#l776"></a>
<span id="l777">        <span class="bp">self</span><span class="o">.</span><span class="n">dest</span> <span class="o">=</span> <span class="n">dest</span></span><a href="#l777"></a>
<span id="l778">        <span class="bp">self</span><span class="o">.</span><span class="n">nargs</span> <span class="o">=</span> <span class="n">nargs</span></span><a href="#l778"></a>
<span id="l779">        <span class="bp">self</span><span class="o">.</span><span class="n">const</span> <span class="o">=</span> <span class="n">const</span></span><a href="#l779"></a>
<span id="l780">        <span class="bp">self</span><span class="o">.</span><span class="n">default</span> <span class="o">=</span> <span class="n">default</span></span><a href="#l780"></a>
<span id="l781">        <span class="bp">self</span><span class="o">.</span><span class="n">type</span> <span class="o">=</span> <span class="nb">type</span></span><a href="#l781"></a>
<span id="l782">        <span class="bp">self</span><span class="o">.</span><span class="n">choices</span> <span class="o">=</span> <span class="n">choices</span></span><a href="#l782"></a>
<span id="l783">        <span class="bp">self</span><span class="o">.</span><span class="n">required</span> <span class="o">=</span> <span class="n">required</span></span><a href="#l783"></a>
<span id="l784">        <span class="bp">self</span><span class="o">.</span><span class="n">help</span> <span class="o">=</span> <span class="n">help</span></span><a href="#l784"></a>
<span id="l785">        <span class="bp">self</span><span class="o">.</span><span class="n">metavar</span> <span class="o">=</span> <span class="n">metavar</span></span><a href="#l785"></a>
<span id="l786"></span><a href="#l786"></a>
<span id="l787">    <span class="k">def</span> <span class="nf">_get_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l787"></a>
<span id="l788">        <span class="n">names</span> <span class="o">=</span> <span class="p">[</span></span><a href="#l788"></a>
<span id="l789">            <span class="s">&#39;option_strings&#39;</span><span class="p">,</span></span><a href="#l789"></a>
<span id="l790">            <span class="s">&#39;dest&#39;</span><span class="p">,</span></span><a href="#l790"></a>
<span id="l791">            <span class="s">&#39;nargs&#39;</span><span class="p">,</span></span><a href="#l791"></a>
<span id="l792">            <span class="s">&#39;const&#39;</span><span class="p">,</span></span><a href="#l792"></a>
<span id="l793">            <span class="s">&#39;default&#39;</span><span class="p">,</span></span><a href="#l793"></a>
<span id="l794">            <span class="s">&#39;type&#39;</span><span class="p">,</span></span><a href="#l794"></a>
<span id="l795">            <span class="s">&#39;choices&#39;</span><span class="p">,</span></span><a href="#l795"></a>
<span id="l796">            <span class="s">&#39;help&#39;</span><span class="p">,</span></span><a href="#l796"></a>
<span id="l797">            <span class="s">&#39;metavar&#39;</span><span class="p">,</span></span><a href="#l797"></a>
<span id="l798">        <span class="p">]</span></span><a href="#l798"></a>
<span id="l799">        <span class="k">return</span> <span class="p">[(</span><span class="n">name</span><span class="p">,</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">))</span> <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">names</span><span class="p">]</span></span><a href="#l799"></a>
<span id="l800"></span><a href="#l800"></a>
<span id="l801">    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parser</span><span class="p">,</span> <span class="n">namespace</span><span class="p">,</span> <span class="n">values</span><span class="p">,</span> <span class="n">option_string</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l801"></a>
<span id="l802">        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s">&#39;.__call__() not defined&#39;</span><span class="p">))</span></span><a href="#l802"></a>
<span id="l803"></span><a href="#l803"></a>
<span id="l804"></span><a href="#l804"></a>
<span id="l805"><span class="k">class</span> <span class="nc">_StoreAction</span><span class="p">(</span><span class="n">Action</span><span class="p">):</span></span><a href="#l805"></a>
<span id="l806"></span><a href="#l806"></a>
<span id="l807">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l807"></a>
<span id="l808">                 <span class="n">option_strings</span><span class="p">,</span></span><a href="#l808"></a>
<span id="l809">                 <span class="n">dest</span><span class="p">,</span></span><a href="#l809"></a>
<span id="l810">                 <span class="n">nargs</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l810"></a>
<span id="l811">                 <span class="n">const</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l811"></a>
<span id="l812">                 <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l812"></a>
<span id="l813">                 <span class="nb">type</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l813"></a>
<span id="l814">                 <span class="n">choices</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l814"></a>
<span id="l815">                 <span class="n">required</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></span><a href="#l815"></a>
<span id="l816">                 <span class="n">help</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l816"></a>
<span id="l817">                 <span class="n">metavar</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l817"></a>
<span id="l818">        <span class="k">if</span> <span class="n">nargs</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l818"></a>
<span id="l819">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;nargs for store actions must be &gt; 0; if you &#39;</span></span><a href="#l819"></a>
<span id="l820">                             <span class="s">&#39;have nothing to store, actions such as store &#39;</span></span><a href="#l820"></a>
<span id="l821">                             <span class="s">&#39;true or store const may be more appropriate&#39;</span><span class="p">)</span></span><a href="#l821"></a>
<span id="l822">        <span class="k">if</span> <span class="n">const</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="n">nargs</span> <span class="o">!=</span> <span class="n">OPTIONAL</span><span class="p">:</span></span><a href="#l822"></a>
<span id="l823">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;nargs must be </span><span class="si">%r</span><span class="s"> to supply const&#39;</span> <span class="o">%</span> <span class="n">OPTIONAL</span><span class="p">)</span></span><a href="#l823"></a>
<span id="l824">        <span class="nb">super</span><span class="p">(</span><span class="n">_StoreAction</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span></span><a href="#l824"></a>
<span id="l825">            <span class="n">option_strings</span><span class="o">=</span><span class="n">option_strings</span><span class="p">,</span></span><a href="#l825"></a>
<span id="l826">            <span class="n">dest</span><span class="o">=</span><span class="n">dest</span><span class="p">,</span></span><a href="#l826"></a>
<span id="l827">            <span class="n">nargs</span><span class="o">=</span><span class="n">nargs</span><span class="p">,</span></span><a href="#l827"></a>
<span id="l828">            <span class="n">const</span><span class="o">=</span><span class="n">const</span><span class="p">,</span></span><a href="#l828"></a>
<span id="l829">            <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">,</span></span><a href="#l829"></a>
<span id="l830">            <span class="nb">type</span><span class="o">=</span><span class="nb">type</span><span class="p">,</span></span><a href="#l830"></a>
<span id="l831">            <span class="n">choices</span><span class="o">=</span><span class="n">choices</span><span class="p">,</span></span><a href="#l831"></a>
<span id="l832">            <span class="n">required</span><span class="o">=</span><span class="n">required</span><span class="p">,</span></span><a href="#l832"></a>
<span id="l833">            <span class="n">help</span><span class="o">=</span><span class="n">help</span><span class="p">,</span></span><a href="#l833"></a>
<span id="l834">            <span class="n">metavar</span><span class="o">=</span><span class="n">metavar</span><span class="p">)</span></span><a href="#l834"></a>
<span id="l835"></span><a href="#l835"></a>
<span id="l836">    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parser</span><span class="p">,</span> <span class="n">namespace</span><span class="p">,</span> <span class="n">values</span><span class="p">,</span> <span class="n">option_string</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l836"></a>
<span id="l837">        <span class="nb">setattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">dest</span><span class="p">,</span> <span class="n">values</span><span class="p">)</span></span><a href="#l837"></a>
<span id="l838"></span><a href="#l838"></a>
<span id="l839"></span><a href="#l839"></a>
<span id="l840"><span class="k">class</span> <span class="nc">_StoreConstAction</span><span class="p">(</span><span class="n">Action</span><span class="p">):</span></span><a href="#l840"></a>
<span id="l841"></span><a href="#l841"></a>
<span id="l842">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l842"></a>
<span id="l843">                 <span class="n">option_strings</span><span class="p">,</span></span><a href="#l843"></a>
<span id="l844">                 <span class="n">dest</span><span class="p">,</span></span><a href="#l844"></a>
<span id="l845">                 <span class="n">const</span><span class="p">,</span></span><a href="#l845"></a>
<span id="l846">                 <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l846"></a>
<span id="l847">                 <span class="n">required</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></span><a href="#l847"></a>
<span id="l848">                 <span class="n">help</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l848"></a>
<span id="l849">                 <span class="n">metavar</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l849"></a>
<span id="l850">        <span class="nb">super</span><span class="p">(</span><span class="n">_StoreConstAction</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span></span><a href="#l850"></a>
<span id="l851">            <span class="n">option_strings</span><span class="o">=</span><span class="n">option_strings</span><span class="p">,</span></span><a href="#l851"></a>
<span id="l852">            <span class="n">dest</span><span class="o">=</span><span class="n">dest</span><span class="p">,</span></span><a href="#l852"></a>
<span id="l853">            <span class="n">nargs</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span></span><a href="#l853"></a>
<span id="l854">            <span class="n">const</span><span class="o">=</span><span class="n">const</span><span class="p">,</span></span><a href="#l854"></a>
<span id="l855">            <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">,</span></span><a href="#l855"></a>
<span id="l856">            <span class="n">required</span><span class="o">=</span><span class="n">required</span><span class="p">,</span></span><a href="#l856"></a>
<span id="l857">            <span class="n">help</span><span class="o">=</span><span class="n">help</span><span class="p">)</span></span><a href="#l857"></a>
<span id="l858"></span><a href="#l858"></a>
<span id="l859">    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parser</span><span class="p">,</span> <span class="n">namespace</span><span class="p">,</span> <span class="n">values</span><span class="p">,</span> <span class="n">option_string</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l859"></a>
<span id="l860">        <span class="nb">setattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">dest</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">const</span><span class="p">)</span></span><a href="#l860"></a>
<span id="l861"></span><a href="#l861"></a>
<span id="l862"></span><a href="#l862"></a>
<span id="l863"><span class="k">class</span> <span class="nc">_StoreTrueAction</span><span class="p">(</span><span class="n">_StoreConstAction</span><span class="p">):</span></span><a href="#l863"></a>
<span id="l864"></span><a href="#l864"></a>
<span id="l865">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l865"></a>
<span id="l866">                 <span class="n">option_strings</span><span class="p">,</span></span><a href="#l866"></a>
<span id="l867">                 <span class="n">dest</span><span class="p">,</span></span><a href="#l867"></a>
<span id="l868">                 <span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></span><a href="#l868"></a>
<span id="l869">                 <span class="n">required</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></span><a href="#l869"></a>
<span id="l870">                 <span class="n">help</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l870"></a>
<span id="l871">        <span class="nb">super</span><span class="p">(</span><span class="n">_StoreTrueAction</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span></span><a href="#l871"></a>
<span id="l872">            <span class="n">option_strings</span><span class="o">=</span><span class="n">option_strings</span><span class="p">,</span></span><a href="#l872"></a>
<span id="l873">            <span class="n">dest</span><span class="o">=</span><span class="n">dest</span><span class="p">,</span></span><a href="#l873"></a>
<span id="l874">            <span class="n">const</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span></span><a href="#l874"></a>
<span id="l875">            <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">,</span></span><a href="#l875"></a>
<span id="l876">            <span class="n">required</span><span class="o">=</span><span class="n">required</span><span class="p">,</span></span><a href="#l876"></a>
<span id="l877">            <span class="n">help</span><span class="o">=</span><span class="n">help</span><span class="p">)</span></span><a href="#l877"></a>
<span id="l878"></span><a href="#l878"></a>
<span id="l879"></span><a href="#l879"></a>
<span id="l880"><span class="k">class</span> <span class="nc">_StoreFalseAction</span><span class="p">(</span><span class="n">_StoreConstAction</span><span class="p">):</span></span><a href="#l880"></a>
<span id="l881"></span><a href="#l881"></a>
<span id="l882">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l882"></a>
<span id="l883">                 <span class="n">option_strings</span><span class="p">,</span></span><a href="#l883"></a>
<span id="l884">                 <span class="n">dest</span><span class="p">,</span></span><a href="#l884"></a>
<span id="l885">                 <span class="n">default</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span></span><a href="#l885"></a>
<span id="l886">                 <span class="n">required</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></span><a href="#l886"></a>
<span id="l887">                 <span class="n">help</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l887"></a>
<span id="l888">        <span class="nb">super</span><span class="p">(</span><span class="n">_StoreFalseAction</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span></span><a href="#l888"></a>
<span id="l889">            <span class="n">option_strings</span><span class="o">=</span><span class="n">option_strings</span><span class="p">,</span></span><a href="#l889"></a>
<span id="l890">            <span class="n">dest</span><span class="o">=</span><span class="n">dest</span><span class="p">,</span></span><a href="#l890"></a>
<span id="l891">            <span class="n">const</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></span><a href="#l891"></a>
<span id="l892">            <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">,</span></span><a href="#l892"></a>
<span id="l893">            <span class="n">required</span><span class="o">=</span><span class="n">required</span><span class="p">,</span></span><a href="#l893"></a>
<span id="l894">            <span class="n">help</span><span class="o">=</span><span class="n">help</span><span class="p">)</span></span><a href="#l894"></a>
<span id="l895"></span><a href="#l895"></a>
<span id="l896"></span><a href="#l896"></a>
<span id="l897"><span class="k">class</span> <span class="nc">_AppendAction</span><span class="p">(</span><span class="n">Action</span><span class="p">):</span></span><a href="#l897"></a>
<span id="l898"></span><a href="#l898"></a>
<span id="l899">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l899"></a>
<span id="l900">                 <span class="n">option_strings</span><span class="p">,</span></span><a href="#l900"></a>
<span id="l901">                 <span class="n">dest</span><span class="p">,</span></span><a href="#l901"></a>
<span id="l902">                 <span class="n">nargs</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l902"></a>
<span id="l903">                 <span class="n">const</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l903"></a>
<span id="l904">                 <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l904"></a>
<span id="l905">                 <span class="nb">type</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l905"></a>
<span id="l906">                 <span class="n">choices</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l906"></a>
<span id="l907">                 <span class="n">required</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></span><a href="#l907"></a>
<span id="l908">                 <span class="n">help</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l908"></a>
<span id="l909">                 <span class="n">metavar</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l909"></a>
<span id="l910">        <span class="k">if</span> <span class="n">nargs</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l910"></a>
<span id="l911">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;nargs for append actions must be &gt; 0; if arg &#39;</span></span><a href="#l911"></a>
<span id="l912">                             <span class="s">&#39;strings are not supplying the value to append, &#39;</span></span><a href="#l912"></a>
<span id="l913">                             <span class="s">&#39;the append const action may be more appropriate&#39;</span><span class="p">)</span></span><a href="#l913"></a>
<span id="l914">        <span class="k">if</span> <span class="n">const</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="n">nargs</span> <span class="o">!=</span> <span class="n">OPTIONAL</span><span class="p">:</span></span><a href="#l914"></a>
<span id="l915">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;nargs must be </span><span class="si">%r</span><span class="s"> to supply const&#39;</span> <span class="o">%</span> <span class="n">OPTIONAL</span><span class="p">)</span></span><a href="#l915"></a>
<span id="l916">        <span class="nb">super</span><span class="p">(</span><span class="n">_AppendAction</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span></span><a href="#l916"></a>
<span id="l917">            <span class="n">option_strings</span><span class="o">=</span><span class="n">option_strings</span><span class="p">,</span></span><a href="#l917"></a>
<span id="l918">            <span class="n">dest</span><span class="o">=</span><span class="n">dest</span><span class="p">,</span></span><a href="#l918"></a>
<span id="l919">            <span class="n">nargs</span><span class="o">=</span><span class="n">nargs</span><span class="p">,</span></span><a href="#l919"></a>
<span id="l920">            <span class="n">const</span><span class="o">=</span><span class="n">const</span><span class="p">,</span></span><a href="#l920"></a>
<span id="l921">            <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">,</span></span><a href="#l921"></a>
<span id="l922">            <span class="nb">type</span><span class="o">=</span><span class="nb">type</span><span class="p">,</span></span><a href="#l922"></a>
<span id="l923">            <span class="n">choices</span><span class="o">=</span><span class="n">choices</span><span class="p">,</span></span><a href="#l923"></a>
<span id="l924">            <span class="n">required</span><span class="o">=</span><span class="n">required</span><span class="p">,</span></span><a href="#l924"></a>
<span id="l925">            <span class="n">help</span><span class="o">=</span><span class="n">help</span><span class="p">,</span></span><a href="#l925"></a>
<span id="l926">            <span class="n">metavar</span><span class="o">=</span><span class="n">metavar</span><span class="p">)</span></span><a href="#l926"></a>
<span id="l927"></span><a href="#l927"></a>
<span id="l928">    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parser</span><span class="p">,</span> <span class="n">namespace</span><span class="p">,</span> <span class="n">values</span><span class="p">,</span> <span class="n">option_string</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l928"></a>
<span id="l929">        <span class="n">items</span> <span class="o">=</span> <span class="n">_copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">_ensure_value</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">dest</span><span class="p">,</span> <span class="p">[]))</span></span><a href="#l929"></a>
<span id="l930">        <span class="n">items</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">values</span><span class="p">)</span></span><a href="#l930"></a>
<span id="l931">        <span class="nb">setattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">dest</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span></span><a href="#l931"></a>
<span id="l932"></span><a href="#l932"></a>
<span id="l933"></span><a href="#l933"></a>
<span id="l934"><span class="k">class</span> <span class="nc">_AppendConstAction</span><span class="p">(</span><span class="n">Action</span><span class="p">):</span></span><a href="#l934"></a>
<span id="l935"></span><a href="#l935"></a>
<span id="l936">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l936"></a>
<span id="l937">                 <span class="n">option_strings</span><span class="p">,</span></span><a href="#l937"></a>
<span id="l938">                 <span class="n">dest</span><span class="p">,</span></span><a href="#l938"></a>
<span id="l939">                 <span class="n">const</span><span class="p">,</span></span><a href="#l939"></a>
<span id="l940">                 <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l940"></a>
<span id="l941">                 <span class="n">required</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></span><a href="#l941"></a>
<span id="l942">                 <span class="n">help</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l942"></a>
<span id="l943">                 <span class="n">metavar</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l943"></a>
<span id="l944">        <span class="nb">super</span><span class="p">(</span><span class="n">_AppendConstAction</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span></span><a href="#l944"></a>
<span id="l945">            <span class="n">option_strings</span><span class="o">=</span><span class="n">option_strings</span><span class="p">,</span></span><a href="#l945"></a>
<span id="l946">            <span class="n">dest</span><span class="o">=</span><span class="n">dest</span><span class="p">,</span></span><a href="#l946"></a>
<span id="l947">            <span class="n">nargs</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span></span><a href="#l947"></a>
<span id="l948">            <span class="n">const</span><span class="o">=</span><span class="n">const</span><span class="p">,</span></span><a href="#l948"></a>
<span id="l949">            <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">,</span></span><a href="#l949"></a>
<span id="l950">            <span class="n">required</span><span class="o">=</span><span class="n">required</span><span class="p">,</span></span><a href="#l950"></a>
<span id="l951">            <span class="n">help</span><span class="o">=</span><span class="n">help</span><span class="p">,</span></span><a href="#l951"></a>
<span id="l952">            <span class="n">metavar</span><span class="o">=</span><span class="n">metavar</span><span class="p">)</span></span><a href="#l952"></a>
<span id="l953"></span><a href="#l953"></a>
<span id="l954">    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parser</span><span class="p">,</span> <span class="n">namespace</span><span class="p">,</span> <span class="n">values</span><span class="p">,</span> <span class="n">option_string</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l954"></a>
<span id="l955">        <span class="n">items</span> <span class="o">=</span> <span class="n">_copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">_ensure_value</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">dest</span><span class="p">,</span> <span class="p">[]))</span></span><a href="#l955"></a>
<span id="l956">        <span class="n">items</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">const</span><span class="p">)</span></span><a href="#l956"></a>
<span id="l957">        <span class="nb">setattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">dest</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span></span><a href="#l957"></a>
<span id="l958"></span><a href="#l958"></a>
<span id="l959"></span><a href="#l959"></a>
<span id="l960"><span class="k">class</span> <span class="nc">_CountAction</span><span class="p">(</span><span class="n">Action</span><span class="p">):</span></span><a href="#l960"></a>
<span id="l961"></span><a href="#l961"></a>
<span id="l962">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l962"></a>
<span id="l963">                 <span class="n">option_strings</span><span class="p">,</span></span><a href="#l963"></a>
<span id="l964">                 <span class="n">dest</span><span class="p">,</span></span><a href="#l964"></a>
<span id="l965">                 <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l965"></a>
<span id="l966">                 <span class="n">required</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></span><a href="#l966"></a>
<span id="l967">                 <span class="n">help</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l967"></a>
<span id="l968">        <span class="nb">super</span><span class="p">(</span><span class="n">_CountAction</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span></span><a href="#l968"></a>
<span id="l969">            <span class="n">option_strings</span><span class="o">=</span><span class="n">option_strings</span><span class="p">,</span></span><a href="#l969"></a>
<span id="l970">            <span class="n">dest</span><span class="o">=</span><span class="n">dest</span><span class="p">,</span></span><a href="#l970"></a>
<span id="l971">            <span class="n">nargs</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span></span><a href="#l971"></a>
<span id="l972">            <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">,</span></span><a href="#l972"></a>
<span id="l973">            <span class="n">required</span><span class="o">=</span><span class="n">required</span><span class="p">,</span></span><a href="#l973"></a>
<span id="l974">            <span class="n">help</span><span class="o">=</span><span class="n">help</span><span class="p">)</span></span><a href="#l974"></a>
<span id="l975"></span><a href="#l975"></a>
<span id="l976">    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parser</span><span class="p">,</span> <span class="n">namespace</span><span class="p">,</span> <span class="n">values</span><span class="p">,</span> <span class="n">option_string</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l976"></a>
<span id="l977">        <span class="n">new_count</span> <span class="o">=</span> <span class="n">_ensure_value</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">dest</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span></span><a href="#l977"></a>
<span id="l978">        <span class="nb">setattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">dest</span><span class="p">,</span> <span class="n">new_count</span><span class="p">)</span></span><a href="#l978"></a>
<span id="l979"></span><a href="#l979"></a>
<span id="l980"></span><a href="#l980"></a>
<span id="l981"><span class="k">class</span> <span class="nc">_HelpAction</span><span class="p">(</span><span class="n">Action</span><span class="p">):</span></span><a href="#l981"></a>
<span id="l982"></span><a href="#l982"></a>
<span id="l983">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l983"></a>
<span id="l984">                 <span class="n">option_strings</span><span class="p">,</span></span><a href="#l984"></a>
<span id="l985">                 <span class="n">dest</span><span class="o">=</span><span class="n">SUPPRESS</span><span class="p">,</span></span><a href="#l985"></a>
<span id="l986">                 <span class="n">default</span><span class="o">=</span><span class="n">SUPPRESS</span><span class="p">,</span></span><a href="#l986"></a>
<span id="l987">                 <span class="n">help</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l987"></a>
<span id="l988">        <span class="nb">super</span><span class="p">(</span><span class="n">_HelpAction</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span></span><a href="#l988"></a>
<span id="l989">            <span class="n">option_strings</span><span class="o">=</span><span class="n">option_strings</span><span class="p">,</span></span><a href="#l989"></a>
<span id="l990">            <span class="n">dest</span><span class="o">=</span><span class="n">dest</span><span class="p">,</span></span><a href="#l990"></a>
<span id="l991">            <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">,</span></span><a href="#l991"></a>
<span id="l992">            <span class="n">nargs</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span></span><a href="#l992"></a>
<span id="l993">            <span class="n">help</span><span class="o">=</span><span class="n">help</span><span class="p">)</span></span><a href="#l993"></a>
<span id="l994"></span><a href="#l994"></a>
<span id="l995">    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parser</span><span class="p">,</span> <span class="n">namespace</span><span class="p">,</span> <span class="n">values</span><span class="p">,</span> <span class="n">option_string</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l995"></a>
<span id="l996">        <span class="n">parser</span><span class="o">.</span><span class="n">print_help</span><span class="p">()</span></span><a href="#l996"></a>
<span id="l997">        <span class="n">parser</span><span class="o">.</span><span class="n">exit</span><span class="p">()</span></span><a href="#l997"></a>
<span id="l998"></span><a href="#l998"></a>
<span id="l999"></span><a href="#l999"></a>
<span id="l1000"><span class="k">class</span> <span class="nc">_VersionAction</span><span class="p">(</span><span class="n">Action</span><span class="p">):</span></span><a href="#l1000"></a>
<span id="l1001"></span><a href="#l1001"></a>
<span id="l1002">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l1002"></a>
<span id="l1003">                 <span class="n">option_strings</span><span class="p">,</span></span><a href="#l1003"></a>
<span id="l1004">                 <span class="n">version</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1004"></a>
<span id="l1005">                 <span class="n">dest</span><span class="o">=</span><span class="n">SUPPRESS</span><span class="p">,</span></span><a href="#l1005"></a>
<span id="l1006">                 <span class="n">default</span><span class="o">=</span><span class="n">SUPPRESS</span><span class="p">,</span></span><a href="#l1006"></a>
<span id="l1007">                 <span class="n">help</span><span class="o">=</span><span class="s">&quot;show program&#39;s version number and exit&quot;</span><span class="p">):</span></span><a href="#l1007"></a>
<span id="l1008">        <span class="nb">super</span><span class="p">(</span><span class="n">_VersionAction</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span></span><a href="#l1008"></a>
<span id="l1009">            <span class="n">option_strings</span><span class="o">=</span><span class="n">option_strings</span><span class="p">,</span></span><a href="#l1009"></a>
<span id="l1010">            <span class="n">dest</span><span class="o">=</span><span class="n">dest</span><span class="p">,</span></span><a href="#l1010"></a>
<span id="l1011">            <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">,</span></span><a href="#l1011"></a>
<span id="l1012">            <span class="n">nargs</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span></span><a href="#l1012"></a>
<span id="l1013">            <span class="n">help</span><span class="o">=</span><span class="n">help</span><span class="p">)</span></span><a href="#l1013"></a>
<span id="l1014">        <span class="bp">self</span><span class="o">.</span><span class="n">version</span> <span class="o">=</span> <span class="n">version</span></span><a href="#l1014"></a>
<span id="l1015"></span><a href="#l1015"></a>
<span id="l1016">    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parser</span><span class="p">,</span> <span class="n">namespace</span><span class="p">,</span> <span class="n">values</span><span class="p">,</span> <span class="n">option_string</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1016"></a>
<span id="l1017">        <span class="n">version</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">version</span></span><a href="#l1017"></a>
<span id="l1018">        <span class="k">if</span> <span class="n">version</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1018"></a>
<span id="l1019">            <span class="n">version</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">version</span></span><a href="#l1019"></a>
<span id="l1020">        <span class="n">formatter</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">_get_formatter</span><span class="p">()</span></span><a href="#l1020"></a>
<span id="l1021">        <span class="n">formatter</span><span class="o">.</span><span class="n">add_text</span><span class="p">(</span><span class="n">version</span><span class="p">)</span></span><a href="#l1021"></a>
<span id="l1022">        <span class="n">parser</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="n">message</span><span class="o">=</span><span class="n">formatter</span><span class="o">.</span><span class="n">format_help</span><span class="p">())</span></span><a href="#l1022"></a>
<span id="l1023"></span><a href="#l1023"></a>
<span id="l1024"></span><a href="#l1024"></a>
<span id="l1025"><span class="k">class</span> <span class="nc">_SubParsersAction</span><span class="p">(</span><span class="n">Action</span><span class="p">):</span></span><a href="#l1025"></a>
<span id="l1026"></span><a href="#l1026"></a>
<span id="l1027">    <span class="k">class</span> <span class="nc">_ChoicesPseudoAction</span><span class="p">(</span><span class="n">Action</span><span class="p">):</span></span><a href="#l1027"></a>
<span id="l1028"></span><a href="#l1028"></a>
<span id="l1029">        <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">help</span><span class="p">):</span></span><a href="#l1029"></a>
<span id="l1030">            <span class="n">sup</span> <span class="o">=</span> <span class="nb">super</span><span class="p">(</span><span class="n">_SubParsersAction</span><span class="o">.</span><span class="n">_ChoicesPseudoAction</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span></span><a href="#l1030"></a>
<span id="l1031">            <span class="n">sup</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="n">option_strings</span><span class="o">=</span><span class="p">[],</span> <span class="n">dest</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="n">help</span><span class="p">)</span></span><a href="#l1031"></a>
<span id="l1032"></span><a href="#l1032"></a>
<span id="l1033">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l1033"></a>
<span id="l1034">                 <span class="n">option_strings</span><span class="p">,</span></span><a href="#l1034"></a>
<span id="l1035">                 <span class="n">prog</span><span class="p">,</span></span><a href="#l1035"></a>
<span id="l1036">                 <span class="n">parser_class</span><span class="p">,</span></span><a href="#l1036"></a>
<span id="l1037">                 <span class="n">dest</span><span class="o">=</span><span class="n">SUPPRESS</span><span class="p">,</span></span><a href="#l1037"></a>
<span id="l1038">                 <span class="n">help</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1038"></a>
<span id="l1039">                 <span class="n">metavar</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1039"></a>
<span id="l1040"></span><a href="#l1040"></a>
<span id="l1041">        <span class="bp">self</span><span class="o">.</span><span class="n">_prog_prefix</span> <span class="o">=</span> <span class="n">prog</span></span><a href="#l1041"></a>
<span id="l1042">        <span class="bp">self</span><span class="o">.</span><span class="n">_parser_class</span> <span class="o">=</span> <span class="n">parser_class</span></span><a href="#l1042"></a>
<span id="l1043">        <span class="bp">self</span><span class="o">.</span><span class="n">_name_parser_map</span> <span class="o">=</span> <span class="n">_collections</span><span class="o">.</span><span class="n">OrderedDict</span><span class="p">()</span></span><a href="#l1043"></a>
<span id="l1044">        <span class="bp">self</span><span class="o">.</span><span class="n">_choices_actions</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1044"></a>
<span id="l1045"></span><a href="#l1045"></a>
<span id="l1046">        <span class="nb">super</span><span class="p">(</span><span class="n">_SubParsersAction</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span></span><a href="#l1046"></a>
<span id="l1047">            <span class="n">option_strings</span><span class="o">=</span><span class="n">option_strings</span><span class="p">,</span></span><a href="#l1047"></a>
<span id="l1048">            <span class="n">dest</span><span class="o">=</span><span class="n">dest</span><span class="p">,</span></span><a href="#l1048"></a>
<span id="l1049">            <span class="n">nargs</span><span class="o">=</span><span class="n">PARSER</span><span class="p">,</span></span><a href="#l1049"></a>
<span id="l1050">            <span class="n">choices</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_name_parser_map</span><span class="p">,</span></span><a href="#l1050"></a>
<span id="l1051">            <span class="n">help</span><span class="o">=</span><span class="n">help</span><span class="p">,</span></span><a href="#l1051"></a>
<span id="l1052">            <span class="n">metavar</span><span class="o">=</span><span class="n">metavar</span><span class="p">)</span></span><a href="#l1052"></a>
<span id="l1053"></span><a href="#l1053"></a>
<span id="l1054">    <span class="k">def</span> <span class="nf">add_parser</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span></span><a href="#l1054"></a>
<span id="l1055">        <span class="c"># set prog from the existing prefix</span></span><a href="#l1055"></a>
<span id="l1056">        <span class="k">if</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;prog&#39;</span><span class="p">)</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1056"></a>
<span id="l1057">            <span class="n">kwargs</span><span class="p">[</span><span class="s">&#39;prog&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s"> </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_prog_prefix</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span></span><a href="#l1057"></a>
<span id="l1058"></span><a href="#l1058"></a>
<span id="l1059">        <span class="c"># create a pseudo-action to hold the choice help</span></span><a href="#l1059"></a>
<span id="l1060">        <span class="k">if</span> <span class="s">&#39;help&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span></span><a href="#l1060"></a>
<span id="l1061">            <span class="n">help</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s">&#39;help&#39;</span><span class="p">)</span></span><a href="#l1061"></a>
<span id="l1062">            <span class="n">choice_action</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ChoicesPseudoAction</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">help</span><span class="p">)</span></span><a href="#l1062"></a>
<span id="l1063">            <span class="bp">self</span><span class="o">.</span><span class="n">_choices_actions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">choice_action</span><span class="p">)</span></span><a href="#l1063"></a>
<span id="l1064"></span><a href="#l1064"></a>
<span id="l1065">        <span class="c"># create the parser and add it to the map</span></span><a href="#l1065"></a>
<span id="l1066">        <span class="n">parser</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_class</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span></span><a href="#l1066"></a>
<span id="l1067">        <span class="bp">self</span><span class="o">.</span><span class="n">_name_parser_map</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">parser</span></span><a href="#l1067"></a>
<span id="l1068">        <span class="k">return</span> <span class="n">parser</span></span><a href="#l1068"></a>
<span id="l1069"></span><a href="#l1069"></a>
<span id="l1070">    <span class="k">def</span> <span class="nf">_get_subactions</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1070"></a>
<span id="l1071">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_choices_actions</span></span><a href="#l1071"></a>
<span id="l1072"></span><a href="#l1072"></a>
<span id="l1073">    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parser</span><span class="p">,</span> <span class="n">namespace</span><span class="p">,</span> <span class="n">values</span><span class="p">,</span> <span class="n">option_string</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1073"></a>
<span id="l1074">        <span class="n">parser_name</span> <span class="o">=</span> <span class="n">values</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l1074"></a>
<span id="l1075">        <span class="n">arg_strings</span> <span class="o">=</span> <span class="n">values</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span></span><a href="#l1075"></a>
<span id="l1076"></span><a href="#l1076"></a>
<span id="l1077">        <span class="c"># set the parser name if requested</span></span><a href="#l1077"></a>
<span id="l1078">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">dest</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">SUPPRESS</span><span class="p">:</span></span><a href="#l1078"></a>
<span id="l1079">            <span class="nb">setattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">dest</span><span class="p">,</span> <span class="n">parser_name</span><span class="p">)</span></span><a href="#l1079"></a>
<span id="l1080"></span><a href="#l1080"></a>
<span id="l1081">        <span class="c"># select the parser</span></span><a href="#l1081"></a>
<span id="l1082">        <span class="k">try</span><span class="p">:</span></span><a href="#l1082"></a>
<span id="l1083">            <span class="n">parser</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name_parser_map</span><span class="p">[</span><span class="n">parser_name</span><span class="p">]</span></span><a href="#l1083"></a>
<span id="l1084">        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span></span><a href="#l1084"></a>
<span id="l1085">            <span class="n">tup</span> <span class="o">=</span> <span class="n">parser_name</span><span class="p">,</span> <span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_name_parser_map</span><span class="p">)</span></span><a href="#l1085"></a>
<span id="l1086">            <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;unknown parser </span><span class="si">%r</span><span class="s"> (choices: </span><span class="si">%s</span><span class="s">)&#39;</span><span class="p">)</span> <span class="o">%</span> <span class="n">tup</span></span><a href="#l1086"></a>
<span id="l1087">            <span class="k">raise</span> <span class="n">ArgumentError</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></span><a href="#l1087"></a>
<span id="l1088"></span><a href="#l1088"></a>
<span id="l1089">        <span class="c"># parse all the remaining options into the namespace</span></span><a href="#l1089"></a>
<span id="l1090">        <span class="c"># store any unrecognized options on the object, so that the top</span></span><a href="#l1090"></a>
<span id="l1091">        <span class="c"># level parser can decide what to do with them</span></span><a href="#l1091"></a>
<span id="l1092">        <span class="n">namespace</span><span class="p">,</span> <span class="n">arg_strings</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_known_args</span><span class="p">(</span><span class="n">arg_strings</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span></span><a href="#l1092"></a>
<span id="l1093">        <span class="k">if</span> <span class="n">arg_strings</span><span class="p">:</span></span><a href="#l1093"></a>
<span id="l1094">            <span class="nb">vars</span><span class="p">(</span><span class="n">namespace</span><span class="p">)</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">_UNRECOGNIZED_ARGS_ATTR</span><span class="p">,</span> <span class="p">[])</span></span><a href="#l1094"></a>
<span id="l1095">            <span class="nb">getattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">_UNRECOGNIZED_ARGS_ATTR</span><span class="p">)</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">arg_strings</span><span class="p">)</span></span><a href="#l1095"></a>
<span id="l1096"></span><a href="#l1096"></a>
<span id="l1097"></span><a href="#l1097"></a>
<span id="l1098"><span class="c"># ==============</span></span><a href="#l1098"></a>
<span id="l1099"><span class="c"># Type classes</span></span><a href="#l1099"></a>
<span id="l1100"><span class="c"># ==============</span></span><a href="#l1100"></a>
<span id="l1101"></span><a href="#l1101"></a>
<span id="l1102"><span class="k">class</span> <span class="nc">FileType</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l1102"></a>
<span id="l1103">    <span class="sd">&quot;&quot;&quot;Factory for creating file object types</span></span><a href="#l1103"></a>
<span id="l1104"></span><a href="#l1104"></a>
<span id="l1105"><span class="sd">    Instances of FileType are typically passed as type= arguments to the</span></span><a href="#l1105"></a>
<span id="l1106"><span class="sd">    ArgumentParser add_argument() method.</span></span><a href="#l1106"></a>
<span id="l1107"></span><a href="#l1107"></a>
<span id="l1108"><span class="sd">    Keyword Arguments:</span></span><a href="#l1108"></a>
<span id="l1109"><span class="sd">        - mode -- A string indicating how the file is to be opened. Accepts the</span></span><a href="#l1109"></a>
<span id="l1110"><span class="sd">            same values as the builtin open() function.</span></span><a href="#l1110"></a>
<span id="l1111"><span class="sd">        - bufsize -- The file&#39;s desired buffer size. Accepts the same values as</span></span><a href="#l1111"></a>
<span id="l1112"><span class="sd">            the builtin open() function.</span></span><a href="#l1112"></a>
<span id="l1113"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l1113"></a>
<span id="l1114"></span><a href="#l1114"></a>
<span id="l1115">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s">&#39;r&#39;</span><span class="p">,</span> <span class="n">bufsize</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span></span><a href="#l1115"></a>
<span id="l1116">        <span class="bp">self</span><span class="o">.</span><span class="n">_mode</span> <span class="o">=</span> <span class="n">mode</span></span><a href="#l1116"></a>
<span id="l1117">        <span class="bp">self</span><span class="o">.</span><span class="n">_bufsize</span> <span class="o">=</span> <span class="n">bufsize</span></span><a href="#l1117"></a>
<span id="l1118"></span><a href="#l1118"></a>
<span id="l1119">    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">string</span><span class="p">):</span></span><a href="#l1119"></a>
<span id="l1120">        <span class="c"># the special argument &quot;-&quot; means sys.std{in,out}</span></span><a href="#l1120"></a>
<span id="l1121">        <span class="k">if</span> <span class="n">string</span> <span class="o">==</span> <span class="s">&#39;-&#39;</span><span class="p">:</span></span><a href="#l1121"></a>
<span id="l1122">            <span class="k">if</span> <span class="s">&#39;r&#39;</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mode</span><span class="p">:</span></span><a href="#l1122"></a>
<span id="l1123">                <span class="k">return</span> <span class="n">_sys</span><span class="o">.</span><span class="n">stdin</span></span><a href="#l1123"></a>
<span id="l1124">            <span class="k">elif</span> <span class="s">&#39;w&#39;</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mode</span><span class="p">:</span></span><a href="#l1124"></a>
<span id="l1125">                <span class="k">return</span> <span class="n">_sys</span><span class="o">.</span><span class="n">stdout</span></span><a href="#l1125"></a>
<span id="l1126">            <span class="k">else</span><span class="p">:</span></span><a href="#l1126"></a>
<span id="l1127">                <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;argument &quot;-&quot; with mode </span><span class="si">%r</span><span class="s">&#39;</span><span class="p">)</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mode</span></span><a href="#l1127"></a>
<span id="l1128">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span></span><a href="#l1128"></a>
<span id="l1129"></span><a href="#l1129"></a>
<span id="l1130">        <span class="c"># all other arguments are used as file names</span></span><a href="#l1130"></a>
<span id="l1131">        <span class="k">try</span><span class="p">:</span></span><a href="#l1131"></a>
<span id="l1132">            <span class="k">return</span> <span class="nb">open</span><span class="p">(</span><span class="n">string</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mode</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bufsize</span><span class="p">)</span></span><a href="#l1132"></a>
<span id="l1133">        <span class="k">except</span> <span class="ne">IOError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span></span><a href="#l1133"></a>
<span id="l1134">            <span class="n">message</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&quot;can&#39;t open &#39;</span><span class="si">%s</span><span class="s">&#39;: </span><span class="si">%s</span><span class="s">&quot;</span><span class="p">)</span></span><a href="#l1134"></a>
<span id="l1135">            <span class="k">raise</span> <span class="n">ArgumentTypeError</span><span class="p">(</span><span class="n">message</span> <span class="o">%</span> <span class="p">(</span><span class="n">string</span><span class="p">,</span> <span class="n">e</span><span class="p">))</span></span><a href="#l1135"></a>
<span id="l1136"></span><a href="#l1136"></a>
<span id="l1137">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1137"></a>
<span id="l1138">        <span class="n">args</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mode</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bufsize</span></span><a href="#l1138"></a>
<span id="l1139">        <span class="n">args_str</span> <span class="o">=</span> <span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">args</span> <span class="k">if</span> <span class="n">arg</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span></span><a href="#l1139"></a>
<span id="l1140">        <span class="k">return</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">(</span><span class="si">%s</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__name__</span><span class="p">,</span> <span class="n">args_str</span><span class="p">)</span></span><a href="#l1140"></a>
<span id="l1141"></span><a href="#l1141"></a>
<span id="l1142"><span class="c"># ===========================</span></span><a href="#l1142"></a>
<span id="l1143"><span class="c"># Optional and Positional Parsing</span></span><a href="#l1143"></a>
<span id="l1144"><span class="c"># ===========================</span></span><a href="#l1144"></a>
<span id="l1145"></span><a href="#l1145"></a>
<span id="l1146"><span class="k">class</span> <span class="nc">Namespace</span><span class="p">(</span><span class="n">_AttributeHolder</span><span class="p">):</span></span><a href="#l1146"></a>
<span id="l1147">    <span class="sd">&quot;&quot;&quot;Simple object for storing attributes.</span></span><a href="#l1147"></a>
<span id="l1148"></span><a href="#l1148"></a>
<span id="l1149"><span class="sd">    Implements equality by attribute names and values, and provides a simple</span></span><a href="#l1149"></a>
<span id="l1150"><span class="sd">    string representation.</span></span><a href="#l1150"></a>
<span id="l1151"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l1151"></a>
<span id="l1152"></span><a href="#l1152"></a>
<span id="l1153">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span></span><a href="#l1153"></a>
<span id="l1154">        <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span></span><a href="#l1154"></a>
<span id="l1155">            <span class="nb">setattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">[</span><span class="n">name</span><span class="p">])</span></span><a href="#l1155"></a>
<span id="l1156"></span><a href="#l1156"></a>
<span id="l1157">    <span class="n">__hash__</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1157"></a>
<span id="l1158"></span><a href="#l1158"></a>
<span id="l1159">    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1159"></a>
<span id="l1160">        <span class="k">return</span> <span class="nb">vars</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">==</span> <span class="nb">vars</span><span class="p">(</span><span class="n">other</span><span class="p">)</span></span><a href="#l1160"></a>
<span id="l1161"></span><a href="#l1161"></a>
<span id="l1162">    <span class="k">def</span> <span class="nf">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1162"></a>
<span id="l1163">        <span class="k">return</span> <span class="ow">not</span> <span class="p">(</span><span class="bp">self</span> <span class="o">==</span> <span class="n">other</span><span class="p">)</span></span><a href="#l1163"></a>
<span id="l1164"></span><a href="#l1164"></a>
<span id="l1165">    <span class="k">def</span> <span class="nf">__contains__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></span><a href="#l1165"></a>
<span id="l1166">        <span class="k">return</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__dict__</span></span><a href="#l1166"></a>
<span id="l1167"></span><a href="#l1167"></a>
<span id="l1168"></span><a href="#l1168"></a>
<span id="l1169"><span class="k">class</span> <span class="nc">_ActionsContainer</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l1169"></a>
<span id="l1170"></span><a href="#l1170"></a>
<span id="l1171">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l1171"></a>
<span id="l1172">                 <span class="n">description</span><span class="p">,</span></span><a href="#l1172"></a>
<span id="l1173">                 <span class="n">prefix_chars</span><span class="p">,</span></span><a href="#l1173"></a>
<span id="l1174">                 <span class="n">argument_default</span><span class="p">,</span></span><a href="#l1174"></a>
<span id="l1175">                 <span class="n">conflict_handler</span><span class="p">):</span></span><a href="#l1175"></a>
<span id="l1176">        <span class="nb">super</span><span class="p">(</span><span class="n">_ActionsContainer</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">()</span></span><a href="#l1176"></a>
<span id="l1177"></span><a href="#l1177"></a>
<span id="l1178">        <span class="bp">self</span><span class="o">.</span><span class="n">description</span> <span class="o">=</span> <span class="n">description</span></span><a href="#l1178"></a>
<span id="l1179">        <span class="bp">self</span><span class="o">.</span><span class="n">argument_default</span> <span class="o">=</span> <span class="n">argument_default</span></span><a href="#l1179"></a>
<span id="l1180">        <span class="bp">self</span><span class="o">.</span><span class="n">prefix_chars</span> <span class="o">=</span> <span class="n">prefix_chars</span></span><a href="#l1180"></a>
<span id="l1181">        <span class="bp">self</span><span class="o">.</span><span class="n">conflict_handler</span> <span class="o">=</span> <span class="n">conflict_handler</span></span><a href="#l1181"></a>
<span id="l1182"></span><a href="#l1182"></a>
<span id="l1183">        <span class="c"># set up registries</span></span><a href="#l1183"></a>
<span id="l1184">        <span class="bp">self</span><span class="o">.</span><span class="n">_registries</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l1184"></a>
<span id="l1185"></span><a href="#l1185"></a>
<span id="l1186">        <span class="c"># register actions</span></span><a href="#l1186"></a>
<span id="l1187">        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="s">&#39;action&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="n">_StoreAction</span><span class="p">)</span></span><a href="#l1187"></a>
<span id="l1188">        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="s">&#39;action&#39;</span><span class="p">,</span> <span class="s">&#39;store&#39;</span><span class="p">,</span> <span class="n">_StoreAction</span><span class="p">)</span></span><a href="#l1188"></a>
<span id="l1189">        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="s">&#39;action&#39;</span><span class="p">,</span> <span class="s">&#39;store_const&#39;</span><span class="p">,</span> <span class="n">_StoreConstAction</span><span class="p">)</span></span><a href="#l1189"></a>
<span id="l1190">        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="s">&#39;action&#39;</span><span class="p">,</span> <span class="s">&#39;store_true&#39;</span><span class="p">,</span> <span class="n">_StoreTrueAction</span><span class="p">)</span></span><a href="#l1190"></a>
<span id="l1191">        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="s">&#39;action&#39;</span><span class="p">,</span> <span class="s">&#39;store_false&#39;</span><span class="p">,</span> <span class="n">_StoreFalseAction</span><span class="p">)</span></span><a href="#l1191"></a>
<span id="l1192">        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="s">&#39;action&#39;</span><span class="p">,</span> <span class="s">&#39;append&#39;</span><span class="p">,</span> <span class="n">_AppendAction</span><span class="p">)</span></span><a href="#l1192"></a>
<span id="l1193">        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="s">&#39;action&#39;</span><span class="p">,</span> <span class="s">&#39;append_const&#39;</span><span class="p">,</span> <span class="n">_AppendConstAction</span><span class="p">)</span></span><a href="#l1193"></a>
<span id="l1194">        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="s">&#39;action&#39;</span><span class="p">,</span> <span class="s">&#39;count&#39;</span><span class="p">,</span> <span class="n">_CountAction</span><span class="p">)</span></span><a href="#l1194"></a>
<span id="l1195">        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="s">&#39;action&#39;</span><span class="p">,</span> <span class="s">&#39;help&#39;</span><span class="p">,</span> <span class="n">_HelpAction</span><span class="p">)</span></span><a href="#l1195"></a>
<span id="l1196">        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="s">&#39;action&#39;</span><span class="p">,</span> <span class="s">&#39;version&#39;</span><span class="p">,</span> <span class="n">_VersionAction</span><span class="p">)</span></span><a href="#l1196"></a>
<span id="l1197">        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="s">&#39;action&#39;</span><span class="p">,</span> <span class="s">&#39;parsers&#39;</span><span class="p">,</span> <span class="n">_SubParsersAction</span><span class="p">)</span></span><a href="#l1197"></a>
<span id="l1198"></span><a href="#l1198"></a>
<span id="l1199">        <span class="c"># raise an exception if the conflict handler is invalid</span></span><a href="#l1199"></a>
<span id="l1200">        <span class="bp">self</span><span class="o">.</span><span class="n">_get_handler</span><span class="p">()</span></span><a href="#l1200"></a>
<span id="l1201"></span><a href="#l1201"></a>
<span id="l1202">        <span class="c"># action storage</span></span><a href="#l1202"></a>
<span id="l1203">        <span class="bp">self</span><span class="o">.</span><span class="n">_actions</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1203"></a>
<span id="l1204">        <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l1204"></a>
<span id="l1205"></span><a href="#l1205"></a>
<span id="l1206">        <span class="c"># groups</span></span><a href="#l1206"></a>
<span id="l1207">        <span class="bp">self</span><span class="o">.</span><span class="n">_action_groups</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1207"></a>
<span id="l1208">        <span class="bp">self</span><span class="o">.</span><span class="n">_mutually_exclusive_groups</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1208"></a>
<span id="l1209"></span><a href="#l1209"></a>
<span id="l1210">        <span class="c"># defaults storage</span></span><a href="#l1210"></a>
<span id="l1211">        <span class="bp">self</span><span class="o">.</span><span class="n">_defaults</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l1211"></a>
<span id="l1212"></span><a href="#l1212"></a>
<span id="l1213">        <span class="c"># determines whether an &quot;option&quot; looks like a negative number</span></span><a href="#l1213"></a>
<span id="l1214">        <span class="bp">self</span><span class="o">.</span><span class="n">_negative_number_matcher</span> <span class="o">=</span> <span class="n">_re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;^-\d+$|^-\d*\.\d+$&#39;</span><span class="p">)</span></span><a href="#l1214"></a>
<span id="l1215"></span><a href="#l1215"></a>
<span id="l1216">        <span class="c"># whether or not there are any optionals that look like negative</span></span><a href="#l1216"></a>
<span id="l1217">        <span class="c"># numbers -- uses a list so it can be shared and edited</span></span><a href="#l1217"></a>
<span id="l1218">        <span class="bp">self</span><span class="o">.</span><span class="n">_has_negative_number_optionals</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1218"></a>
<span id="l1219"></span><a href="#l1219"></a>
<span id="l1220">    <span class="c"># ====================</span></span><a href="#l1220"></a>
<span id="l1221">    <span class="c"># Registration methods</span></span><a href="#l1221"></a>
<span id="l1222">    <span class="c"># ====================</span></span><a href="#l1222"></a>
<span id="l1223">    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">registry_name</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="nb">object</span><span class="p">):</span></span><a href="#l1223"></a>
<span id="l1224">        <span class="n">registry</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_registries</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">registry_name</span><span class="p">,</span> <span class="p">{})</span></span><a href="#l1224"></a>
<span id="l1225">        <span class="n">registry</span><span class="p">[</span><span class="n">value</span><span class="p">]</span> <span class="o">=</span> <span class="nb">object</span></span><a href="#l1225"></a>
<span id="l1226"></span><a href="#l1226"></a>
<span id="l1227">    <span class="k">def</span> <span class="nf">_registry_get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">registry_name</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1227"></a>
<span id="l1228">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_registries</span><span class="p">[</span><span class="n">registry_name</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">default</span><span class="p">)</span></span><a href="#l1228"></a>
<span id="l1229"></span><a href="#l1229"></a>
<span id="l1230">    <span class="c"># ==================================</span></span><a href="#l1230"></a>
<span id="l1231">    <span class="c"># Namespace default accessor methods</span></span><a href="#l1231"></a>
<span id="l1232">    <span class="c"># ==================================</span></span><a href="#l1232"></a>
<span id="l1233">    <span class="k">def</span> <span class="nf">set_defaults</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span></span><a href="#l1233"></a>
<span id="l1234">        <span class="bp">self</span><span class="o">.</span><span class="n">_defaults</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span></span><a href="#l1234"></a>
<span id="l1235"></span><a href="#l1235"></a>
<span id="l1236">        <span class="c"># if these defaults match any existing arguments, replace</span></span><a href="#l1236"></a>
<span id="l1237">        <span class="c"># the previous default on the object with the new one</span></span><a href="#l1237"></a>
<span id="l1238">        <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_actions</span><span class="p">:</span></span><a href="#l1238"></a>
<span id="l1239">            <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">dest</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span></span><a href="#l1239"></a>
<span id="l1240">                <span class="n">action</span><span class="o">.</span><span class="n">default</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="n">action</span><span class="o">.</span><span class="n">dest</span><span class="p">]</span></span><a href="#l1240"></a>
<span id="l1241"></span><a href="#l1241"></a>
<span id="l1242">    <span class="k">def</span> <span class="nf">get_default</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dest</span><span class="p">):</span></span><a href="#l1242"></a>
<span id="l1243">        <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_actions</span><span class="p">:</span></span><a href="#l1243"></a>
<span id="l1244">            <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">dest</span> <span class="o">==</span> <span class="n">dest</span> <span class="ow">and</span> <span class="n">action</span><span class="o">.</span><span class="n">default</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1244"></a>
<span id="l1245">                <span class="k">return</span> <span class="n">action</span><span class="o">.</span><span class="n">default</span></span><a href="#l1245"></a>
<span id="l1246">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_defaults</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">dest</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l1246"></a>
<span id="l1247"></span><a href="#l1247"></a>
<span id="l1248"></span><a href="#l1248"></a>
<span id="l1249">    <span class="c"># =======================</span></span><a href="#l1249"></a>
<span id="l1250">    <span class="c"># Adding argument actions</span></span><a href="#l1250"></a>
<span id="l1251">    <span class="c"># =======================</span></span><a href="#l1251"></a>
<span id="l1252">    <span class="k">def</span> <span class="nf">add_argument</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span></span><a href="#l1252"></a>
<span id="l1253">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1253"></a>
<span id="l1254"><span class="sd">        add_argument(dest, ..., name=value, ...)</span></span><a href="#l1254"></a>
<span id="l1255"><span class="sd">        add_argument(option_string, option_string, ..., name=value, ...)</span></span><a href="#l1255"></a>
<span id="l1256"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1256"></a>
<span id="l1257"></span><a href="#l1257"></a>
<span id="l1258">        <span class="c"># if no positional args are supplied or only one is supplied and</span></span><a href="#l1258"></a>
<span id="l1259">        <span class="c"># it doesn&#39;t look like an option string, parse a positional</span></span><a href="#l1259"></a>
<span id="l1260">        <span class="c"># argument</span></span><a href="#l1260"></a>
<span id="l1261">        <span class="n">chars</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">prefix_chars</span></span><a href="#l1261"></a>
<span id="l1262">        <span class="k">if</span> <span class="ow">not</span> <span class="n">args</span> <span class="ow">or</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span> <span class="ow">and</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">chars</span><span class="p">:</span></span><a href="#l1262"></a>
<span id="l1263">            <span class="k">if</span> <span class="n">args</span> <span class="ow">and</span> <span class="s">&#39;dest&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span></span><a href="#l1263"></a>
<span id="l1264">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;dest supplied twice for positional argument&#39;</span><span class="p">)</span></span><a href="#l1264"></a>
<span id="l1265">            <span class="n">kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_positional_kwargs</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span></span><a href="#l1265"></a>
<span id="l1266"></span><a href="#l1266"></a>
<span id="l1267">        <span class="c"># otherwise, we&#39;re adding an optional argument</span></span><a href="#l1267"></a>
<span id="l1268">        <span class="k">else</span><span class="p">:</span></span><a href="#l1268"></a>
<span id="l1269">            <span class="n">kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_optional_kwargs</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span></span><a href="#l1269"></a>
<span id="l1270"></span><a href="#l1270"></a>
<span id="l1271">        <span class="c"># if no default was supplied, use the parser-level default</span></span><a href="#l1271"></a>
<span id="l1272">        <span class="k">if</span> <span class="s">&#39;default&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span></span><a href="#l1272"></a>
<span id="l1273">            <span class="n">dest</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s">&#39;dest&#39;</span><span class="p">]</span></span><a href="#l1273"></a>
<span id="l1274">            <span class="k">if</span> <span class="n">dest</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_defaults</span><span class="p">:</span></span><a href="#l1274"></a>
<span id="l1275">                <span class="n">kwargs</span><span class="p">[</span><span class="s">&#39;default&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_defaults</span><span class="p">[</span><span class="n">dest</span><span class="p">]</span></span><a href="#l1275"></a>
<span id="l1276">            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">argument_default</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1276"></a>
<span id="l1277">                <span class="n">kwargs</span><span class="p">[</span><span class="s">&#39;default&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">argument_default</span></span><a href="#l1277"></a>
<span id="l1278"></span><a href="#l1278"></a>
<span id="l1279">        <span class="c"># create the action object, and add it to the parser</span></span><a href="#l1279"></a>
<span id="l1280">        <span class="n">action_class</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pop_action_class</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span></span><a href="#l1280"></a>
<span id="l1281">        <span class="k">if</span> <span class="ow">not</span> <span class="n">_callable</span><span class="p">(</span><span class="n">action_class</span><span class="p">):</span></span><a href="#l1281"></a>
<span id="l1282">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;unknown action &quot;</span><span class="si">%s</span><span class="s">&quot;&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">action_class</span><span class="p">,))</span></span><a href="#l1282"></a>
<span id="l1283">        <span class="n">action</span> <span class="o">=</span> <span class="n">action_class</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span></span><a href="#l1283"></a>
<span id="l1284"></span><a href="#l1284"></a>
<span id="l1285">        <span class="c"># raise an error if the action type is not callable</span></span><a href="#l1285"></a>
<span id="l1286">        <span class="n">type_func</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_registry_get</span><span class="p">(</span><span class="s">&#39;type&#39;</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">type</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">type</span><span class="p">)</span></span><a href="#l1286"></a>
<span id="l1287">        <span class="k">if</span> <span class="ow">not</span> <span class="n">_callable</span><span class="p">(</span><span class="n">type_func</span><span class="p">):</span></span><a href="#l1287"></a>
<span id="l1288">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%r</span><span class="s"> is not callable&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">type_func</span><span class="p">,))</span></span><a href="#l1288"></a>
<span id="l1289"></span><a href="#l1289"></a>
<span id="l1290">        <span class="c"># raise an error if the metavar does not match the type</span></span><a href="#l1290"></a>
<span id="l1291">        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s">&quot;_get_formatter&quot;</span><span class="p">):</span></span><a href="#l1291"></a>
<span id="l1292">            <span class="k">try</span><span class="p">:</span></span><a href="#l1292"></a>
<span id="l1293">                <span class="bp">self</span><span class="o">.</span><span class="n">_get_formatter</span><span class="p">()</span><span class="o">.</span><span class="n">_format_args</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l1293"></a>
<span id="l1294">            <span class="k">except</span> <span class="ne">TypeError</span><span class="p">:</span></span><a href="#l1294"></a>
<span id="l1295">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;length of metavar tuple does not match nargs&quot;</span><span class="p">)</span></span><a href="#l1295"></a>
<span id="l1296"></span><a href="#l1296"></a>
<span id="l1297">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_add_action</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1297"></a>
<span id="l1298"></span><a href="#l1298"></a>
<span id="l1299">    <span class="k">def</span> <span class="nf">add_argument_group</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span></span><a href="#l1299"></a>
<span id="l1300">        <span class="n">group</span> <span class="o">=</span> <span class="n">_ArgumentGroup</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span></span><a href="#l1300"></a>
<span id="l1301">        <span class="bp">self</span><span class="o">.</span><span class="n">_action_groups</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">group</span><span class="p">)</span></span><a href="#l1301"></a>
<span id="l1302">        <span class="k">return</span> <span class="n">group</span></span><a href="#l1302"></a>
<span id="l1303"></span><a href="#l1303"></a>
<span id="l1304">    <span class="k">def</span> <span class="nf">add_mutually_exclusive_group</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span></span><a href="#l1304"></a>
<span id="l1305">        <span class="n">group</span> <span class="o">=</span> <span class="n">_MutuallyExclusiveGroup</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span></span><a href="#l1305"></a>
<span id="l1306">        <span class="bp">self</span><span class="o">.</span><span class="n">_mutually_exclusive_groups</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">group</span><span class="p">)</span></span><a href="#l1306"></a>
<span id="l1307">        <span class="k">return</span> <span class="n">group</span></span><a href="#l1307"></a>
<span id="l1308"></span><a href="#l1308"></a>
<span id="l1309">    <span class="k">def</span> <span class="nf">_add_action</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l1309"></a>
<span id="l1310">        <span class="c"># resolve any conflicts</span></span><a href="#l1310"></a>
<span id="l1311">        <span class="bp">self</span><span class="o">.</span><span class="n">_check_conflict</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1311"></a>
<span id="l1312"></span><a href="#l1312"></a>
<span id="l1313">        <span class="c"># add to actions list</span></span><a href="#l1313"></a>
<span id="l1314">        <span class="bp">self</span><span class="o">.</span><span class="n">_actions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1314"></a>
<span id="l1315">        <span class="n">action</span><span class="o">.</span><span class="n">container</span> <span class="o">=</span> <span class="bp">self</span></span><a href="#l1315"></a>
<span id="l1316"></span><a href="#l1316"></a>
<span id="l1317">        <span class="c"># index the action by any option strings it has</span></span><a href="#l1317"></a>
<span id="l1318">        <span class="k">for</span> <span class="n">option_string</span> <span class="ow">in</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">:</span></span><a href="#l1318"></a>
<span id="l1319">            <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span><span class="p">[</span><span class="n">option_string</span><span class="p">]</span> <span class="o">=</span> <span class="n">action</span></span><a href="#l1319"></a>
<span id="l1320"></span><a href="#l1320"></a>
<span id="l1321">        <span class="c"># set the flag if any option strings look like negative numbers</span></span><a href="#l1321"></a>
<span id="l1322">        <span class="k">for</span> <span class="n">option_string</span> <span class="ow">in</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">:</span></span><a href="#l1322"></a>
<span id="l1323">            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_negative_number_matcher</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">option_string</span><span class="p">):</span></span><a href="#l1323"></a>
<span id="l1324">                <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_has_negative_number_optionals</span><span class="p">:</span></span><a href="#l1324"></a>
<span id="l1325">                    <span class="bp">self</span><span class="o">.</span><span class="n">_has_negative_number_optionals</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span></span><a href="#l1325"></a>
<span id="l1326"></span><a href="#l1326"></a>
<span id="l1327">        <span class="c"># return the created action</span></span><a href="#l1327"></a>
<span id="l1328">        <span class="k">return</span> <span class="n">action</span></span><a href="#l1328"></a>
<span id="l1329"></span><a href="#l1329"></a>
<span id="l1330">    <span class="k">def</span> <span class="nf">_remove_action</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l1330"></a>
<span id="l1331">        <span class="bp">self</span><span class="o">.</span><span class="n">_actions</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1331"></a>
<span id="l1332"></span><a href="#l1332"></a>
<span id="l1333">    <span class="k">def</span> <span class="nf">_add_container_actions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">container</span><span class="p">):</span></span><a href="#l1333"></a>
<span id="l1334">        <span class="c"># collect groups by titles</span></span><a href="#l1334"></a>
<span id="l1335">        <span class="n">title_group_map</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l1335"></a>
<span id="l1336">        <span class="k">for</span> <span class="n">group</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_action_groups</span><span class="p">:</span></span><a href="#l1336"></a>
<span id="l1337">            <span class="k">if</span> <span class="n">group</span><span class="o">.</span><span class="n">title</span> <span class="ow">in</span> <span class="n">title_group_map</span><span class="p">:</span></span><a href="#l1337"></a>
<span id="l1338">                <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;cannot merge actions - two groups are named </span><span class="si">%r</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l1338"></a>
<span id="l1339">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">msg</span> <span class="o">%</span> <span class="p">(</span><span class="n">group</span><span class="o">.</span><span class="n">title</span><span class="p">))</span></span><a href="#l1339"></a>
<span id="l1340">            <span class="n">title_group_map</span><span class="p">[</span><span class="n">group</span><span class="o">.</span><span class="n">title</span><span class="p">]</span> <span class="o">=</span> <span class="n">group</span></span><a href="#l1340"></a>
<span id="l1341"></span><a href="#l1341"></a>
<span id="l1342">        <span class="c"># map each action to its group</span></span><a href="#l1342"></a>
<span id="l1343">        <span class="n">group_map</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l1343"></a>
<span id="l1344">        <span class="k">for</span> <span class="n">group</span> <span class="ow">in</span> <span class="n">container</span><span class="o">.</span><span class="n">_action_groups</span><span class="p">:</span></span><a href="#l1344"></a>
<span id="l1345"></span><a href="#l1345"></a>
<span id="l1346">            <span class="c"># if a group with the title exists, use that, otherwise</span></span><a href="#l1346"></a>
<span id="l1347">            <span class="c"># create a new group matching the container&#39;s group</span></span><a href="#l1347"></a>
<span id="l1348">            <span class="k">if</span> <span class="n">group</span><span class="o">.</span><span class="n">title</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">title_group_map</span><span class="p">:</span></span><a href="#l1348"></a>
<span id="l1349">                <span class="n">title_group_map</span><span class="p">[</span><span class="n">group</span><span class="o">.</span><span class="n">title</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">add_argument_group</span><span class="p">(</span></span><a href="#l1349"></a>
<span id="l1350">                    <span class="n">title</span><span class="o">=</span><span class="n">group</span><span class="o">.</span><span class="n">title</span><span class="p">,</span></span><a href="#l1350"></a>
<span id="l1351">                    <span class="n">description</span><span class="o">=</span><span class="n">group</span><span class="o">.</span><span class="n">description</span><span class="p">,</span></span><a href="#l1351"></a>
<span id="l1352">                    <span class="n">conflict_handler</span><span class="o">=</span><span class="n">group</span><span class="o">.</span><span class="n">conflict_handler</span><span class="p">)</span></span><a href="#l1352"></a>
<span id="l1353"></span><a href="#l1353"></a>
<span id="l1354">            <span class="c"># map the actions to their new group</span></span><a href="#l1354"></a>
<span id="l1355">            <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">group</span><span class="o">.</span><span class="n">_group_actions</span><span class="p">:</span></span><a href="#l1355"></a>
<span id="l1356">                <span class="n">group_map</span><span class="p">[</span><span class="n">action</span><span class="p">]</span> <span class="o">=</span> <span class="n">title_group_map</span><span class="p">[</span><span class="n">group</span><span class="o">.</span><span class="n">title</span><span class="p">]</span></span><a href="#l1356"></a>
<span id="l1357"></span><a href="#l1357"></a>
<span id="l1358">        <span class="c"># add container&#39;s mutually exclusive groups</span></span><a href="#l1358"></a>
<span id="l1359">        <span class="c"># NOTE: if add_mutually_exclusive_group ever gains title= and</span></span><a href="#l1359"></a>
<span id="l1360">        <span class="c"># description= then this code will need to be expanded as above</span></span><a href="#l1360"></a>
<span id="l1361">        <span class="k">for</span> <span class="n">group</span> <span class="ow">in</span> <span class="n">container</span><span class="o">.</span><span class="n">_mutually_exclusive_groups</span><span class="p">:</span></span><a href="#l1361"></a>
<span id="l1362">            <span class="n">mutex_group</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">add_mutually_exclusive_group</span><span class="p">(</span></span><a href="#l1362"></a>
<span id="l1363">                <span class="n">required</span><span class="o">=</span><span class="n">group</span><span class="o">.</span><span class="n">required</span><span class="p">)</span></span><a href="#l1363"></a>
<span id="l1364"></span><a href="#l1364"></a>
<span id="l1365">            <span class="c"># map the actions to their new mutex group</span></span><a href="#l1365"></a>
<span id="l1366">            <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">group</span><span class="o">.</span><span class="n">_group_actions</span><span class="p">:</span></span><a href="#l1366"></a>
<span id="l1367">                <span class="n">group_map</span><span class="p">[</span><span class="n">action</span><span class="p">]</span> <span class="o">=</span> <span class="n">mutex_group</span></span><a href="#l1367"></a>
<span id="l1368"></span><a href="#l1368"></a>
<span id="l1369">        <span class="c"># add all actions to this container or their group</span></span><a href="#l1369"></a>
<span id="l1370">        <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">container</span><span class="o">.</span><span class="n">_actions</span><span class="p">:</span></span><a href="#l1370"></a>
<span id="l1371">            <span class="n">group_map</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">_add_action</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1371"></a>
<span id="l1372"></span><a href="#l1372"></a>
<span id="l1373">    <span class="k">def</span> <span class="nf">_get_positional_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dest</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span></span><a href="#l1373"></a>
<span id="l1374">        <span class="c"># make sure required is not specified</span></span><a href="#l1374"></a>
<span id="l1375">        <span class="k">if</span> <span class="s">&#39;required&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span></span><a href="#l1375"></a>
<span id="l1376">            <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&quot;&#39;required&#39; is an invalid argument for positionals&quot;</span><span class="p">)</span></span><a href="#l1376"></a>
<span id="l1377">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span></span><a href="#l1377"></a>
<span id="l1378"></span><a href="#l1378"></a>
<span id="l1379">        <span class="c"># mark positional arguments as required if at least one is</span></span><a href="#l1379"></a>
<span id="l1380">        <span class="c"># always required</span></span><a href="#l1380"></a>
<span id="l1381">        <span class="k">if</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;nargs&#39;</span><span class="p">)</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">[</span><span class="n">OPTIONAL</span><span class="p">,</span> <span class="n">ZERO_OR_MORE</span><span class="p">]:</span></span><a href="#l1381"></a>
<span id="l1382">            <span class="n">kwargs</span><span class="p">[</span><span class="s">&#39;required&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">True</span></span><a href="#l1382"></a>
<span id="l1383">        <span class="k">if</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;nargs&#39;</span><span class="p">)</span> <span class="o">==</span> <span class="n">ZERO_OR_MORE</span> <span class="ow">and</span> <span class="s">&#39;default&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span></span><a href="#l1383"></a>
<span id="l1384">            <span class="n">kwargs</span><span class="p">[</span><span class="s">&#39;required&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">True</span></span><a href="#l1384"></a>
<span id="l1385"></span><a href="#l1385"></a>
<span id="l1386">        <span class="c"># return the keyword arguments with no option strings</span></span><a href="#l1386"></a>
<span id="l1387">        <span class="k">return</span> <span class="nb">dict</span><span class="p">(</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="n">dest</span><span class="p">,</span> <span class="n">option_strings</span><span class="o">=</span><span class="p">[])</span></span><a href="#l1387"></a>
<span id="l1388"></span><a href="#l1388"></a>
<span id="l1389">    <span class="k">def</span> <span class="nf">_get_optional_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span></span><a href="#l1389"></a>
<span id="l1390">        <span class="c"># determine short and long option strings</span></span><a href="#l1390"></a>
<span id="l1391">        <span class="n">option_strings</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1391"></a>
<span id="l1392">        <span class="n">long_option_strings</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1392"></a>
<span id="l1393">        <span class="k">for</span> <span class="n">option_string</span> <span class="ow">in</span> <span class="n">args</span><span class="p">:</span></span><a href="#l1393"></a>
<span id="l1394">            <span class="c"># error on strings that don&#39;t start with an appropriate prefix</span></span><a href="#l1394"></a>
<span id="l1395">            <span class="k">if</span> <span class="ow">not</span> <span class="n">option_string</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">prefix_chars</span><span class="p">:</span></span><a href="#l1395"></a>
<span id="l1396">                <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;invalid option string </span><span class="si">%r</span><span class="s">: &#39;</span></span><a href="#l1396"></a>
<span id="l1397">                        <span class="s">&#39;must start with a character </span><span class="si">%r</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l1397"></a>
<span id="l1398">                <span class="n">tup</span> <span class="o">=</span> <span class="n">option_string</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">prefix_chars</span></span><a href="#l1398"></a>
<span id="l1399">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">msg</span> <span class="o">%</span> <span class="n">tup</span><span class="p">)</span></span><a href="#l1399"></a>
<span id="l1400"></span><a href="#l1400"></a>
<span id="l1401">            <span class="c"># strings starting with two prefix characters are long options</span></span><a href="#l1401"></a>
<span id="l1402">            <span class="n">option_strings</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">option_string</span><span class="p">)</span></span><a href="#l1402"></a>
<span id="l1403">            <span class="k">if</span> <span class="n">option_string</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">prefix_chars</span><span class="p">:</span></span><a href="#l1403"></a>
<span id="l1404">                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">option_string</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l1404"></a>
<span id="l1405">                    <span class="k">if</span> <span class="n">option_string</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">prefix_chars</span><span class="p">:</span></span><a href="#l1405"></a>
<span id="l1406">                        <span class="n">long_option_strings</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">option_string</span><span class="p">)</span></span><a href="#l1406"></a>
<span id="l1407"></span><a href="#l1407"></a>
<span id="l1408">        <span class="c"># infer destination, &#39;--foo-bar&#39; -&gt; &#39;foo_bar&#39; and &#39;-x&#39; -&gt; &#39;x&#39;</span></span><a href="#l1408"></a>
<span id="l1409">        <span class="n">dest</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s">&#39;dest&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l1409"></a>
<span id="l1410">        <span class="k">if</span> <span class="n">dest</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1410"></a>
<span id="l1411">            <span class="k">if</span> <span class="n">long_option_strings</span><span class="p">:</span></span><a href="#l1411"></a>
<span id="l1412">                <span class="n">dest_option_string</span> <span class="o">=</span> <span class="n">long_option_strings</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l1412"></a>
<span id="l1413">            <span class="k">else</span><span class="p">:</span></span><a href="#l1413"></a>
<span id="l1414">                <span class="n">dest_option_string</span> <span class="o">=</span> <span class="n">option_strings</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l1414"></a>
<span id="l1415">            <span class="n">dest</span> <span class="o">=</span> <span class="n">dest_option_string</span><span class="o">.</span><span class="n">lstrip</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">prefix_chars</span><span class="p">)</span></span><a href="#l1415"></a>
<span id="l1416">            <span class="k">if</span> <span class="ow">not</span> <span class="n">dest</span><span class="p">:</span></span><a href="#l1416"></a>
<span id="l1417">                <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;dest= is required for options like </span><span class="si">%r</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l1417"></a>
<span id="l1418">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">msg</span> <span class="o">%</span> <span class="n">option_string</span><span class="p">)</span></span><a href="#l1418"></a>
<span id="l1419">            <span class="n">dest</span> <span class="o">=</span> <span class="n">dest</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;-&#39;</span><span class="p">,</span> <span class="s">&#39;_&#39;</span><span class="p">)</span></span><a href="#l1419"></a>
<span id="l1420"></span><a href="#l1420"></a>
<span id="l1421">        <span class="c"># return the updated keyword arguments</span></span><a href="#l1421"></a>
<span id="l1422">        <span class="k">return</span> <span class="nb">dict</span><span class="p">(</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="n">dest</span><span class="p">,</span> <span class="n">option_strings</span><span class="o">=</span><span class="n">option_strings</span><span class="p">)</span></span><a href="#l1422"></a>
<span id="l1423"></span><a href="#l1423"></a>
<span id="l1424">    <span class="k">def</span> <span class="nf">_pop_action_class</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1424"></a>
<span id="l1425">        <span class="n">action</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s">&#39;action&#39;</span><span class="p">,</span> <span class="n">default</span><span class="p">)</span></span><a href="#l1425"></a>
<span id="l1426">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_registry_get</span><span class="p">(</span><span class="s">&#39;action&#39;</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">action</span><span class="p">)</span></span><a href="#l1426"></a>
<span id="l1427"></span><a href="#l1427"></a>
<span id="l1428">    <span class="k">def</span> <span class="nf">_get_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1428"></a>
<span id="l1429">        <span class="c"># determine function from conflict handler string</span></span><a href="#l1429"></a>
<span id="l1430">        <span class="n">handler_func_name</span> <span class="o">=</span> <span class="s">&#39;_handle_conflict_</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">conflict_handler</span></span><a href="#l1430"></a>
<span id="l1431">        <span class="k">try</span><span class="p">:</span></span><a href="#l1431"></a>
<span id="l1432">            <span class="k">return</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler_func_name</span><span class="p">)</span></span><a href="#l1432"></a>
<span id="l1433">        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></span><a href="#l1433"></a>
<span id="l1434">            <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;invalid conflict_resolution value: </span><span class="si">%r</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l1434"></a>
<span id="l1435">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">msg</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">conflict_handler</span><span class="p">)</span></span><a href="#l1435"></a>
<span id="l1436"></span><a href="#l1436"></a>
<span id="l1437">    <span class="k">def</span> <span class="nf">_check_conflict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l1437"></a>
<span id="l1438"></span><a href="#l1438"></a>
<span id="l1439">        <span class="c"># find all options that conflict with this option</span></span><a href="#l1439"></a>
<span id="l1440">        <span class="n">confl_optionals</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1440"></a>
<span id="l1441">        <span class="k">for</span> <span class="n">option_string</span> <span class="ow">in</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">:</span></span><a href="#l1441"></a>
<span id="l1442">            <span class="k">if</span> <span class="n">option_string</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span><span class="p">:</span></span><a href="#l1442"></a>
<span id="l1443">                <span class="n">confl_optional</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span><span class="p">[</span><span class="n">option_string</span><span class="p">]</span></span><a href="#l1443"></a>
<span id="l1444">                <span class="n">confl_optionals</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">option_string</span><span class="p">,</span> <span class="n">confl_optional</span><span class="p">))</span></span><a href="#l1444"></a>
<span id="l1445"></span><a href="#l1445"></a>
<span id="l1446">        <span class="c"># resolve any conflicts</span></span><a href="#l1446"></a>
<span id="l1447">        <span class="k">if</span> <span class="n">confl_optionals</span><span class="p">:</span></span><a href="#l1447"></a>
<span id="l1448">            <span class="n">conflict_handler</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_handler</span><span class="p">()</span></span><a href="#l1448"></a>
<span id="l1449">            <span class="n">conflict_handler</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">confl_optionals</span><span class="p">)</span></span><a href="#l1449"></a>
<span id="l1450"></span><a href="#l1450"></a>
<span id="l1451">    <span class="k">def</span> <span class="nf">_handle_conflict_error</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">conflicting_actions</span><span class="p">):</span></span><a href="#l1451"></a>
<span id="l1452">        <span class="n">message</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;conflicting option string(s): </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l1452"></a>
<span id="l1453">        <span class="n">conflict_string</span> <span class="o">=</span> <span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">option_string</span></span><a href="#l1453"></a>
<span id="l1454">                                     <span class="k">for</span> <span class="n">option_string</span><span class="p">,</span> <span class="n">action</span></span><a href="#l1454"></a>
<span id="l1455">                                     <span class="ow">in</span> <span class="n">conflicting_actions</span><span class="p">])</span></span><a href="#l1455"></a>
<span id="l1456">        <span class="k">raise</span> <span class="n">ArgumentError</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">message</span> <span class="o">%</span> <span class="n">conflict_string</span><span class="p">)</span></span><a href="#l1456"></a>
<span id="l1457"></span><a href="#l1457"></a>
<span id="l1458">    <span class="k">def</span> <span class="nf">_handle_conflict_resolve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">conflicting_actions</span><span class="p">):</span></span><a href="#l1458"></a>
<span id="l1459"></span><a href="#l1459"></a>
<span id="l1460">        <span class="c"># remove all conflicting options</span></span><a href="#l1460"></a>
<span id="l1461">        <span class="k">for</span> <span class="n">option_string</span><span class="p">,</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">conflicting_actions</span><span class="p">:</span></span><a href="#l1461"></a>
<span id="l1462"></span><a href="#l1462"></a>
<span id="l1463">            <span class="c"># remove the conflicting option</span></span><a href="#l1463"></a>
<span id="l1464">            <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">option_string</span><span class="p">)</span></span><a href="#l1464"></a>
<span id="l1465">            <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">option_string</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l1465"></a>
<span id="l1466"></span><a href="#l1466"></a>
<span id="l1467">            <span class="c"># if the option now has no option string, remove it from the</span></span><a href="#l1467"></a>
<span id="l1468">            <span class="c"># container holding it</span></span><a href="#l1468"></a>
<span id="l1469">            <span class="k">if</span> <span class="ow">not</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">:</span></span><a href="#l1469"></a>
<span id="l1470">                <span class="n">action</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">_remove_action</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1470"></a>
<span id="l1471"></span><a href="#l1471"></a>
<span id="l1472"></span><a href="#l1472"></a>
<span id="l1473"><span class="k">class</span> <span class="nc">_ArgumentGroup</span><span class="p">(</span><span class="n">_ActionsContainer</span><span class="p">):</span></span><a href="#l1473"></a>
<span id="l1474"></span><a href="#l1474"></a>
<span id="l1475">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">container</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span></span><a href="#l1475"></a>
<span id="l1476">        <span class="c"># add any missing keyword arguments by checking the container</span></span><a href="#l1476"></a>
<span id="l1477">        <span class="n">update</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">setdefault</span></span><a href="#l1477"></a>
<span id="l1478">        <span class="n">update</span><span class="p">(</span><span class="s">&#39;conflict_handler&#39;</span><span class="p">,</span> <span class="n">container</span><span class="o">.</span><span class="n">conflict_handler</span><span class="p">)</span></span><a href="#l1478"></a>
<span id="l1479">        <span class="n">update</span><span class="p">(</span><span class="s">&#39;prefix_chars&#39;</span><span class="p">,</span> <span class="n">container</span><span class="o">.</span><span class="n">prefix_chars</span><span class="p">)</span></span><a href="#l1479"></a>
<span id="l1480">        <span class="n">update</span><span class="p">(</span><span class="s">&#39;argument_default&#39;</span><span class="p">,</span> <span class="n">container</span><span class="o">.</span><span class="n">argument_default</span><span class="p">)</span></span><a href="#l1480"></a>
<span id="l1481">        <span class="n">super_init</span> <span class="o">=</span> <span class="nb">super</span><span class="p">(</span><span class="n">_ArgumentGroup</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span></span><a href="#l1481"></a>
<span id="l1482">        <span class="n">super_init</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span></span><a href="#l1482"></a>
<span id="l1483"></span><a href="#l1483"></a>
<span id="l1484">        <span class="c"># group attributes</span></span><a href="#l1484"></a>
<span id="l1485">        <span class="bp">self</span><span class="o">.</span><span class="n">title</span> <span class="o">=</span> <span class="n">title</span></span><a href="#l1485"></a>
<span id="l1486">        <span class="bp">self</span><span class="o">.</span><span class="n">_group_actions</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1486"></a>
<span id="l1487"></span><a href="#l1487"></a>
<span id="l1488">        <span class="c"># share most attributes with the container</span></span><a href="#l1488"></a>
<span id="l1489">        <span class="bp">self</span><span class="o">.</span><span class="n">_registries</span> <span class="o">=</span> <span class="n">container</span><span class="o">.</span><span class="n">_registries</span></span><a href="#l1489"></a>
<span id="l1490">        <span class="bp">self</span><span class="o">.</span><span class="n">_actions</span> <span class="o">=</span> <span class="n">container</span><span class="o">.</span><span class="n">_actions</span></span><a href="#l1490"></a>
<span id="l1491">        <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span> <span class="o">=</span> <span class="n">container</span><span class="o">.</span><span class="n">_option_string_actions</span></span><a href="#l1491"></a>
<span id="l1492">        <span class="bp">self</span><span class="o">.</span><span class="n">_defaults</span> <span class="o">=</span> <span class="n">container</span><span class="o">.</span><span class="n">_defaults</span></span><a href="#l1492"></a>
<span id="l1493">        <span class="bp">self</span><span class="o">.</span><span class="n">_has_negative_number_optionals</span> <span class="o">=</span> \</span><a href="#l1493"></a>
<span id="l1494">            <span class="n">container</span><span class="o">.</span><span class="n">_has_negative_number_optionals</span></span><a href="#l1494"></a>
<span id="l1495">        <span class="bp">self</span><span class="o">.</span><span class="n">_mutually_exclusive_groups</span> <span class="o">=</span> <span class="n">container</span><span class="o">.</span><span class="n">_mutually_exclusive_groups</span></span><a href="#l1495"></a>
<span id="l1496"></span><a href="#l1496"></a>
<span id="l1497">    <span class="k">def</span> <span class="nf">_add_action</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l1497"></a>
<span id="l1498">        <span class="n">action</span> <span class="o">=</span> <span class="nb">super</span><span class="p">(</span><span class="n">_ArgumentGroup</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">_add_action</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1498"></a>
<span id="l1499">        <span class="bp">self</span><span class="o">.</span><span class="n">_group_actions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1499"></a>
<span id="l1500">        <span class="k">return</span> <span class="n">action</span></span><a href="#l1500"></a>
<span id="l1501"></span><a href="#l1501"></a>
<span id="l1502">    <span class="k">def</span> <span class="nf">_remove_action</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l1502"></a>
<span id="l1503">        <span class="nb">super</span><span class="p">(</span><span class="n">_ArgumentGroup</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">_remove_action</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1503"></a>
<span id="l1504">        <span class="bp">self</span><span class="o">.</span><span class="n">_group_actions</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1504"></a>
<span id="l1505"></span><a href="#l1505"></a>
<span id="l1506"></span><a href="#l1506"></a>
<span id="l1507"><span class="k">class</span> <span class="nc">_MutuallyExclusiveGroup</span><span class="p">(</span><span class="n">_ArgumentGroup</span><span class="p">):</span></span><a href="#l1507"></a>
<span id="l1508"></span><a href="#l1508"></a>
<span id="l1509">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">container</span><span class="p">,</span> <span class="n">required</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></span><a href="#l1509"></a>
<span id="l1510">        <span class="nb">super</span><span class="p">(</span><span class="n">_MutuallyExclusiveGroup</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="n">container</span><span class="p">)</span></span><a href="#l1510"></a>
<span id="l1511">        <span class="bp">self</span><span class="o">.</span><span class="n">required</span> <span class="o">=</span> <span class="n">required</span></span><a href="#l1511"></a>
<span id="l1512">        <span class="bp">self</span><span class="o">.</span><span class="n">_container</span> <span class="o">=</span> <span class="n">container</span></span><a href="#l1512"></a>
<span id="l1513"></span><a href="#l1513"></a>
<span id="l1514">    <span class="k">def</span> <span class="nf">_add_action</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l1514"></a>
<span id="l1515">        <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">required</span><span class="p">:</span></span><a href="#l1515"></a>
<span id="l1516">            <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;mutually exclusive arguments must be optional&#39;</span><span class="p">)</span></span><a href="#l1516"></a>
<span id="l1517">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span></span><a href="#l1517"></a>
<span id="l1518">        <span class="n">action</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_container</span><span class="o">.</span><span class="n">_add_action</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1518"></a>
<span id="l1519">        <span class="bp">self</span><span class="o">.</span><span class="n">_group_actions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1519"></a>
<span id="l1520">        <span class="k">return</span> <span class="n">action</span></span><a href="#l1520"></a>
<span id="l1521"></span><a href="#l1521"></a>
<span id="l1522">    <span class="k">def</span> <span class="nf">_remove_action</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l1522"></a>
<span id="l1523">        <span class="bp">self</span><span class="o">.</span><span class="n">_container</span><span class="o">.</span><span class="n">_remove_action</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1523"></a>
<span id="l1524">        <span class="bp">self</span><span class="o">.</span><span class="n">_group_actions</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1524"></a>
<span id="l1525"></span><a href="#l1525"></a>
<span id="l1526"></span><a href="#l1526"></a>
<span id="l1527"><span class="k">class</span> <span class="nc">ArgumentParser</span><span class="p">(</span><span class="n">_AttributeHolder</span><span class="p">,</span> <span class="n">_ActionsContainer</span><span class="p">):</span></span><a href="#l1527"></a>
<span id="l1528">    <span class="sd">&quot;&quot;&quot;Object for parsing command line strings into Python objects.</span></span><a href="#l1528"></a>
<span id="l1529"></span><a href="#l1529"></a>
<span id="l1530"><span class="sd">    Keyword Arguments:</span></span><a href="#l1530"></a>
<span id="l1531"><span class="sd">        - prog -- The name of the program (default: sys.argv[0])</span></span><a href="#l1531"></a>
<span id="l1532"><span class="sd">        - usage -- A usage message (default: auto-generated from arguments)</span></span><a href="#l1532"></a>
<span id="l1533"><span class="sd">        - description -- A description of what the program does</span></span><a href="#l1533"></a>
<span id="l1534"><span class="sd">        - epilog -- Text following the argument descriptions</span></span><a href="#l1534"></a>
<span id="l1535"><span class="sd">        - parents -- Parsers whose arguments should be copied into this one</span></span><a href="#l1535"></a>
<span id="l1536"><span class="sd">        - formatter_class -- HelpFormatter class for printing help messages</span></span><a href="#l1536"></a>
<span id="l1537"><span class="sd">        - prefix_chars -- Characters that prefix optional arguments</span></span><a href="#l1537"></a>
<span id="l1538"><span class="sd">        - fromfile_prefix_chars -- Characters that prefix files containing</span></span><a href="#l1538"></a>
<span id="l1539"><span class="sd">            additional arguments</span></span><a href="#l1539"></a>
<span id="l1540"><span class="sd">        - argument_default -- The default value for all arguments</span></span><a href="#l1540"></a>
<span id="l1541"><span class="sd">        - conflict_handler -- String indicating how to handle conflicts</span></span><a href="#l1541"></a>
<span id="l1542"><span class="sd">        - add_help -- Add a -h/-help option</span></span><a href="#l1542"></a>
<span id="l1543"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l1543"></a>
<span id="l1544"></span><a href="#l1544"></a>
<span id="l1545">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></span><a href="#l1545"></a>
<span id="l1546">                 <span class="n">prog</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1546"></a>
<span id="l1547">                 <span class="n">usage</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1547"></a>
<span id="l1548">                 <span class="n">description</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1548"></a>
<span id="l1549">                 <span class="n">epilog</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1549"></a>
<span id="l1550">                 <span class="n">version</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1550"></a>
<span id="l1551">                 <span class="n">parents</span><span class="o">=</span><span class="p">[],</span></span><a href="#l1551"></a>
<span id="l1552">                 <span class="n">formatter_class</span><span class="o">=</span><span class="n">HelpFormatter</span><span class="p">,</span></span><a href="#l1552"></a>
<span id="l1553">                 <span class="n">prefix_chars</span><span class="o">=</span><span class="s">&#39;-&#39;</span><span class="p">,</span></span><a href="#l1553"></a>
<span id="l1554">                 <span class="n">fromfile_prefix_chars</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1554"></a>
<span id="l1555">                 <span class="n">argument_default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1555"></a>
<span id="l1556">                 <span class="n">conflict_handler</span><span class="o">=</span><span class="s">&#39;error&#39;</span><span class="p">,</span></span><a href="#l1556"></a>
<span id="l1557">                 <span class="n">add_help</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></span><a href="#l1557"></a>
<span id="l1558"></span><a href="#l1558"></a>
<span id="l1559">        <span class="k">if</span> <span class="n">version</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1559"></a>
<span id="l1560">            <span class="kn">import</span> <span class="nn">warnings</span></span><a href="#l1560"></a>
<span id="l1561">            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span></span><a href="#l1561"></a>
<span id="l1562">                <span class="sd">&quot;&quot;&quot;The &quot;version&quot; argument to ArgumentParser is deprecated. &quot;&quot;&quot;</span></span><a href="#l1562"></a>
<span id="l1563">                <span class="sd">&quot;&quot;&quot;Please use &quot;&quot;&quot;</span></span><a href="#l1563"></a>
<span id="l1564">                <span class="sd">&quot;&quot;&quot;&quot;add_argument(..., action=&#39;version&#39;, version=&quot;N&quot;, ...)&quot; &quot;&quot;&quot;</span></span><a href="#l1564"></a>
<span id="l1565">                <span class="sd">&quot;&quot;&quot;instead&quot;&quot;&quot;</span><span class="p">,</span> <span class="ne">DeprecationWarning</span><span class="p">)</span></span><a href="#l1565"></a>
<span id="l1566"></span><a href="#l1566"></a>
<span id="l1567">        <span class="n">superinit</span> <span class="o">=</span> <span class="nb">super</span><span class="p">(</span><span class="n">ArgumentParser</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span></span><a href="#l1567"></a>
<span id="l1568">        <span class="n">superinit</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span></span><a href="#l1568"></a>
<span id="l1569">                  <span class="n">prefix_chars</span><span class="o">=</span><span class="n">prefix_chars</span><span class="p">,</span></span><a href="#l1569"></a>
<span id="l1570">                  <span class="n">argument_default</span><span class="o">=</span><span class="n">argument_default</span><span class="p">,</span></span><a href="#l1570"></a>
<span id="l1571">                  <span class="n">conflict_handler</span><span class="o">=</span><span class="n">conflict_handler</span><span class="p">)</span></span><a href="#l1571"></a>
<span id="l1572"></span><a href="#l1572"></a>
<span id="l1573">        <span class="c"># default setting for prog</span></span><a href="#l1573"></a>
<span id="l1574">        <span class="k">if</span> <span class="n">prog</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1574"></a>
<span id="l1575">            <span class="n">prog</span> <span class="o">=</span> <span class="n">_os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">_sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span></span><a href="#l1575"></a>
<span id="l1576"></span><a href="#l1576"></a>
<span id="l1577">        <span class="bp">self</span><span class="o">.</span><span class="n">prog</span> <span class="o">=</span> <span class="n">prog</span></span><a href="#l1577"></a>
<span id="l1578">        <span class="bp">self</span><span class="o">.</span><span class="n">usage</span> <span class="o">=</span> <span class="n">usage</span></span><a href="#l1578"></a>
<span id="l1579">        <span class="bp">self</span><span class="o">.</span><span class="n">epilog</span> <span class="o">=</span> <span class="n">epilog</span></span><a href="#l1579"></a>
<span id="l1580">        <span class="bp">self</span><span class="o">.</span><span class="n">version</span> <span class="o">=</span> <span class="n">version</span></span><a href="#l1580"></a>
<span id="l1581">        <span class="bp">self</span><span class="o">.</span><span class="n">formatter_class</span> <span class="o">=</span> <span class="n">formatter_class</span></span><a href="#l1581"></a>
<span id="l1582">        <span class="bp">self</span><span class="o">.</span><span class="n">fromfile_prefix_chars</span> <span class="o">=</span> <span class="n">fromfile_prefix_chars</span></span><a href="#l1582"></a>
<span id="l1583">        <span class="bp">self</span><span class="o">.</span><span class="n">add_help</span> <span class="o">=</span> <span class="n">add_help</span></span><a href="#l1583"></a>
<span id="l1584"></span><a href="#l1584"></a>
<span id="l1585">        <span class="n">add_group</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">add_argument_group</span></span><a href="#l1585"></a>
<span id="l1586">        <span class="bp">self</span><span class="o">.</span><span class="n">_positionals</span> <span class="o">=</span> <span class="n">add_group</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s">&#39;positional arguments&#39;</span><span class="p">))</span></span><a href="#l1586"></a>
<span id="l1587">        <span class="bp">self</span><span class="o">.</span><span class="n">_optionals</span> <span class="o">=</span> <span class="n">add_group</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s">&#39;optional arguments&#39;</span><span class="p">))</span></span><a href="#l1587"></a>
<span id="l1588">        <span class="bp">self</span><span class="o">.</span><span class="n">_subparsers</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1588"></a>
<span id="l1589"></span><a href="#l1589"></a>
<span id="l1590">        <span class="c"># register types</span></span><a href="#l1590"></a>
<span id="l1591">        <span class="k">def</span> <span class="nf">identity</span><span class="p">(</span><span class="n">string</span><span class="p">):</span></span><a href="#l1591"></a>
<span id="l1592">            <span class="k">return</span> <span class="n">string</span></span><a href="#l1592"></a>
<span id="l1593">        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="s">&#39;type&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="n">identity</span><span class="p">)</span></span><a href="#l1593"></a>
<span id="l1594"></span><a href="#l1594"></a>
<span id="l1595">        <span class="c"># add help and version arguments if necessary</span></span><a href="#l1595"></a>
<span id="l1596">        <span class="c"># (using explicit default to override global argument_default)</span></span><a href="#l1596"></a>
<span id="l1597">        <span class="n">default_prefix</span> <span class="o">=</span> <span class="s">&#39;-&#39;</span> <span class="k">if</span> <span class="s">&#39;-&#39;</span> <span class="ow">in</span> <span class="n">prefix_chars</span> <span class="k">else</span> <span class="n">prefix_chars</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l1597"></a>
<span id="l1598">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">add_help</span><span class="p">:</span></span><a href="#l1598"></a>
<span id="l1599">            <span class="bp">self</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span></span><a href="#l1599"></a>
<span id="l1600">                <span class="n">default_prefix</span><span class="o">+</span><span class="s">&#39;h&#39;</span><span class="p">,</span> <span class="n">default_prefix</span><span class="o">*</span><span class="mi">2</span><span class="o">+</span><span class="s">&#39;help&#39;</span><span class="p">,</span></span><a href="#l1600"></a>
<span id="l1601">                <span class="n">action</span><span class="o">=</span><span class="s">&#39;help&#39;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="n">SUPPRESS</span><span class="p">,</span></span><a href="#l1601"></a>
<span id="l1602">                <span class="n">help</span><span class="o">=</span><span class="n">_</span><span class="p">(</span><span class="s">&#39;show this help message and exit&#39;</span><span class="p">))</span></span><a href="#l1602"></a>
<span id="l1603">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">version</span><span class="p">:</span></span><a href="#l1603"></a>
<span id="l1604">            <span class="bp">self</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span></span><a href="#l1604"></a>
<span id="l1605">                <span class="n">default_prefix</span><span class="o">+</span><span class="s">&#39;v&#39;</span><span class="p">,</span> <span class="n">default_prefix</span><span class="o">*</span><span class="mi">2</span><span class="o">+</span><span class="s">&#39;version&#39;</span><span class="p">,</span></span><a href="#l1605"></a>
<span id="l1606">                <span class="n">action</span><span class="o">=</span><span class="s">&#39;version&#39;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="n">SUPPRESS</span><span class="p">,</span></span><a href="#l1606"></a>
<span id="l1607">                <span class="n">version</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">version</span><span class="p">,</span></span><a href="#l1607"></a>
<span id="l1608">                <span class="n">help</span><span class="o">=</span><span class="n">_</span><span class="p">(</span><span class="s">&quot;show program&#39;s version number and exit&quot;</span><span class="p">))</span></span><a href="#l1608"></a>
<span id="l1609"></span><a href="#l1609"></a>
<span id="l1610">        <span class="c"># add parent arguments and defaults</span></span><a href="#l1610"></a>
<span id="l1611">        <span class="k">for</span> <span class="n">parent</span> <span class="ow">in</span> <span class="n">parents</span><span class="p">:</span></span><a href="#l1611"></a>
<span id="l1612">            <span class="bp">self</span><span class="o">.</span><span class="n">_add_container_actions</span><span class="p">(</span><span class="n">parent</span><span class="p">)</span></span><a href="#l1612"></a>
<span id="l1613">            <span class="k">try</span><span class="p">:</span></span><a href="#l1613"></a>
<span id="l1614">                <span class="n">defaults</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">_defaults</span></span><a href="#l1614"></a>
<span id="l1615">            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></span><a href="#l1615"></a>
<span id="l1616">                <span class="k">pass</span></span><a href="#l1616"></a>
<span id="l1617">            <span class="k">else</span><span class="p">:</span></span><a href="#l1617"></a>
<span id="l1618">                <span class="bp">self</span><span class="o">.</span><span class="n">_defaults</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">defaults</span><span class="p">)</span></span><a href="#l1618"></a>
<span id="l1619"></span><a href="#l1619"></a>
<span id="l1620">    <span class="c"># =======================</span></span><a href="#l1620"></a>
<span id="l1621">    <span class="c"># Pretty __repr__ methods</span></span><a href="#l1621"></a>
<span id="l1622">    <span class="c"># =======================</span></span><a href="#l1622"></a>
<span id="l1623">    <span class="k">def</span> <span class="nf">_get_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1623"></a>
<span id="l1624">        <span class="n">names</span> <span class="o">=</span> <span class="p">[</span></span><a href="#l1624"></a>
<span id="l1625">            <span class="s">&#39;prog&#39;</span><span class="p">,</span></span><a href="#l1625"></a>
<span id="l1626">            <span class="s">&#39;usage&#39;</span><span class="p">,</span></span><a href="#l1626"></a>
<span id="l1627">            <span class="s">&#39;description&#39;</span><span class="p">,</span></span><a href="#l1627"></a>
<span id="l1628">            <span class="s">&#39;version&#39;</span><span class="p">,</span></span><a href="#l1628"></a>
<span id="l1629">            <span class="s">&#39;formatter_class&#39;</span><span class="p">,</span></span><a href="#l1629"></a>
<span id="l1630">            <span class="s">&#39;conflict_handler&#39;</span><span class="p">,</span></span><a href="#l1630"></a>
<span id="l1631">            <span class="s">&#39;add_help&#39;</span><span class="p">,</span></span><a href="#l1631"></a>
<span id="l1632">        <span class="p">]</span></span><a href="#l1632"></a>
<span id="l1633">        <span class="k">return</span> <span class="p">[(</span><span class="n">name</span><span class="p">,</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">))</span> <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">names</span><span class="p">]</span></span><a href="#l1633"></a>
<span id="l1634"></span><a href="#l1634"></a>
<span id="l1635">    <span class="c"># ==================================</span></span><a href="#l1635"></a>
<span id="l1636">    <span class="c"># Optional/Positional adding methods</span></span><a href="#l1636"></a>
<span id="l1637">    <span class="c"># ==================================</span></span><a href="#l1637"></a>
<span id="l1638">    <span class="k">def</span> <span class="nf">add_subparsers</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span></span><a href="#l1638"></a>
<span id="l1639">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subparsers</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1639"></a>
<span id="l1640">            <span class="bp">self</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s">&#39;cannot have multiple subparser arguments&#39;</span><span class="p">))</span></span><a href="#l1640"></a>
<span id="l1641"></span><a href="#l1641"></a>
<span id="l1642">        <span class="c"># add the parser class to the arguments if it&#39;s not present</span></span><a href="#l1642"></a>
<span id="l1643">        <span class="n">kwargs</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="s">&#39;parser_class&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span></span><a href="#l1643"></a>
<span id="l1644"></span><a href="#l1644"></a>
<span id="l1645">        <span class="k">if</span> <span class="s">&#39;title&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span> <span class="ow">or</span> <span class="s">&#39;description&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span></span><a href="#l1645"></a>
<span id="l1646">            <span class="n">title</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s">&#39;title&#39;</span><span class="p">,</span> <span class="s">&#39;subcommands&#39;</span><span class="p">))</span></span><a href="#l1646"></a>
<span id="l1647">            <span class="n">description</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s">&#39;description&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">))</span></span><a href="#l1647"></a>
<span id="l1648">            <span class="bp">self</span><span class="o">.</span><span class="n">_subparsers</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">add_argument_group</span><span class="p">(</span><span class="n">title</span><span class="p">,</span> <span class="n">description</span><span class="p">)</span></span><a href="#l1648"></a>
<span id="l1649">        <span class="k">else</span><span class="p">:</span></span><a href="#l1649"></a>
<span id="l1650">            <span class="bp">self</span><span class="o">.</span><span class="n">_subparsers</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_positionals</span></span><a href="#l1650"></a>
<span id="l1651"></span><a href="#l1651"></a>
<span id="l1652">        <span class="c"># prog defaults to the usage message of this parser, skipping</span></span><a href="#l1652"></a>
<span id="l1653">        <span class="c"># optional arguments and with no &quot;usage:&quot; prefix</span></span><a href="#l1653"></a>
<span id="l1654">        <span class="k">if</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;prog&#39;</span><span class="p">)</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1654"></a>
<span id="l1655">            <span class="n">formatter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_formatter</span><span class="p">()</span></span><a href="#l1655"></a>
<span id="l1656">            <span class="n">positionals</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_positional_actions</span><span class="p">()</span></span><a href="#l1656"></a>
<span id="l1657">            <span class="n">groups</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mutually_exclusive_groups</span></span><a href="#l1657"></a>
<span id="l1658">            <span class="n">formatter</span><span class="o">.</span><span class="n">add_usage</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">usage</span><span class="p">,</span> <span class="n">positionals</span><span class="p">,</span> <span class="n">groups</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)</span></span><a href="#l1658"></a>
<span id="l1659">            <span class="n">kwargs</span><span class="p">[</span><span class="s">&#39;prog&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">formatter</span><span class="o">.</span><span class="n">format_help</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></span><a href="#l1659"></a>
<span id="l1660"></span><a href="#l1660"></a>
<span id="l1661">        <span class="c"># create the parsers action and add it to the positionals list</span></span><a href="#l1661"></a>
<span id="l1662">        <span class="n">parsers_class</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pop_action_class</span><span class="p">(</span><span class="n">kwargs</span><span class="p">,</span> <span class="s">&#39;parsers&#39;</span><span class="p">)</span></span><a href="#l1662"></a>
<span id="l1663">        <span class="n">action</span> <span class="o">=</span> <span class="n">parsers_class</span><span class="p">(</span><span class="n">option_strings</span><span class="o">=</span><span class="p">[],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span></span><a href="#l1663"></a>
<span id="l1664">        <span class="bp">self</span><span class="o">.</span><span class="n">_subparsers</span><span class="o">.</span><span class="n">_add_action</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1664"></a>
<span id="l1665"></span><a href="#l1665"></a>
<span id="l1666">        <span class="c"># return the created parsers action</span></span><a href="#l1666"></a>
<span id="l1667">        <span class="k">return</span> <span class="n">action</span></span><a href="#l1667"></a>
<span id="l1668"></span><a href="#l1668"></a>
<span id="l1669">    <span class="k">def</span> <span class="nf">_add_action</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l1669"></a>
<span id="l1670">        <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">:</span></span><a href="#l1670"></a>
<span id="l1671">            <span class="bp">self</span><span class="o">.</span><span class="n">_optionals</span><span class="o">.</span><span class="n">_add_action</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1671"></a>
<span id="l1672">        <span class="k">else</span><span class="p">:</span></span><a href="#l1672"></a>
<span id="l1673">            <span class="bp">self</span><span class="o">.</span><span class="n">_positionals</span><span class="o">.</span><span class="n">_add_action</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1673"></a>
<span id="l1674">        <span class="k">return</span> <span class="n">action</span></span><a href="#l1674"></a>
<span id="l1675"></span><a href="#l1675"></a>
<span id="l1676">    <span class="k">def</span> <span class="nf">_get_optional_actions</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1676"></a>
<span id="l1677">        <span class="k">return</span> <span class="p">[</span><span class="n">action</span></span><a href="#l1677"></a>
<span id="l1678">                <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_actions</span></span><a href="#l1678"></a>
<span id="l1679">                <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">]</span></span><a href="#l1679"></a>
<span id="l1680"></span><a href="#l1680"></a>
<span id="l1681">    <span class="k">def</span> <span class="nf">_get_positional_actions</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1681"></a>
<span id="l1682">        <span class="k">return</span> <span class="p">[</span><span class="n">action</span></span><a href="#l1682"></a>
<span id="l1683">                <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_actions</span></span><a href="#l1683"></a>
<span id="l1684">                <span class="k">if</span> <span class="ow">not</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">]</span></span><a href="#l1684"></a>
<span id="l1685"></span><a href="#l1685"></a>
<span id="l1686">    <span class="c"># =====================================</span></span><a href="#l1686"></a>
<span id="l1687">    <span class="c"># Command line argument parsing methods</span></span><a href="#l1687"></a>
<span id="l1688">    <span class="c"># =====================================</span></span><a href="#l1688"></a>
<span id="l1689">    <span class="k">def</span> <span class="nf">parse_args</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1689"></a>
<span id="l1690">        <span class="n">args</span><span class="p">,</span> <span class="n">argv</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parse_known_args</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span></span><a href="#l1690"></a>
<span id="l1691">        <span class="k">if</span> <span class="n">argv</span><span class="p">:</span></span><a href="#l1691"></a>
<span id="l1692">            <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;unrecognized arguments: </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l1692"></a>
<span id="l1693">            <span class="bp">self</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">msg</span> <span class="o">%</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">argv</span><span class="p">))</span></span><a href="#l1693"></a>
<span id="l1694">        <span class="k">return</span> <span class="n">args</span></span><a href="#l1694"></a>
<span id="l1695"></span><a href="#l1695"></a>
<span id="l1696">    <span class="k">def</span> <span class="nf">parse_known_args</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1696"></a>
<span id="l1697">        <span class="k">if</span> <span class="n">args</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1697"></a>
<span id="l1698">            <span class="c"># args default to the system args</span></span><a href="#l1698"></a>
<span id="l1699">            <span class="n">args</span> <span class="o">=</span> <span class="n">_sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span></span><a href="#l1699"></a>
<span id="l1700">        <span class="k">else</span><span class="p">:</span></span><a href="#l1700"></a>
<span id="l1701">            <span class="c"># make sure that args are mutable</span></span><a href="#l1701"></a>
<span id="l1702">            <span class="n">args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">args</span><span class="p">)</span></span><a href="#l1702"></a>
<span id="l1703"></span><a href="#l1703"></a>
<span id="l1704">        <span class="c"># default Namespace built from parser defaults</span></span><a href="#l1704"></a>
<span id="l1705">        <span class="k">if</span> <span class="n">namespace</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1705"></a>
<span id="l1706">            <span class="n">namespace</span> <span class="o">=</span> <span class="n">Namespace</span><span class="p">()</span></span><a href="#l1706"></a>
<span id="l1707"></span><a href="#l1707"></a>
<span id="l1708">        <span class="c"># add any action defaults that aren&#39;t present</span></span><a href="#l1708"></a>
<span id="l1709">        <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_actions</span><span class="p">:</span></span><a href="#l1709"></a>
<span id="l1710">            <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">dest</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">SUPPRESS</span><span class="p">:</span></span><a href="#l1710"></a>
<span id="l1711">                <span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">dest</span><span class="p">):</span></span><a href="#l1711"></a>
<span id="l1712">                    <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">default</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">SUPPRESS</span><span class="p">:</span></span><a href="#l1712"></a>
<span id="l1713">                        <span class="nb">setattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">dest</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">default</span><span class="p">)</span></span><a href="#l1713"></a>
<span id="l1714"></span><a href="#l1714"></a>
<span id="l1715">        <span class="c"># add any parser defaults that aren&#39;t present</span></span><a href="#l1715"></a>
<span id="l1716">        <span class="k">for</span> <span class="n">dest</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_defaults</span><span class="p">:</span></span><a href="#l1716"></a>
<span id="l1717">            <span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">dest</span><span class="p">):</span></span><a href="#l1717"></a>
<span id="l1718">                <span class="nb">setattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">dest</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_defaults</span><span class="p">[</span><span class="n">dest</span><span class="p">])</span></span><a href="#l1718"></a>
<span id="l1719"></span><a href="#l1719"></a>
<span id="l1720">        <span class="c"># parse the arguments and exit if there are any errors</span></span><a href="#l1720"></a>
<span id="l1721">        <span class="k">try</span><span class="p">:</span></span><a href="#l1721"></a>
<span id="l1722">            <span class="n">namespace</span><span class="p">,</span> <span class="n">args</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_known_args</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span></span><a href="#l1722"></a>
<span id="l1723">            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">_UNRECOGNIZED_ARGS_ATTR</span><span class="p">):</span></span><a href="#l1723"></a>
<span id="l1724">                <span class="n">args</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">_UNRECOGNIZED_ARGS_ATTR</span><span class="p">))</span></span><a href="#l1724"></a>
<span id="l1725">                <span class="nb">delattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">_UNRECOGNIZED_ARGS_ATTR</span><span class="p">)</span></span><a href="#l1725"></a>
<span id="l1726">            <span class="k">return</span> <span class="n">namespace</span><span class="p">,</span> <span class="n">args</span></span><a href="#l1726"></a>
<span id="l1727">        <span class="k">except</span> <span class="n">ArgumentError</span><span class="p">:</span></span><a href="#l1727"></a>
<span id="l1728">            <span class="n">err</span> <span class="o">=</span> <span class="n">_sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span></span><a href="#l1728"></a>
<span id="l1729">            <span class="bp">self</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">err</span><span class="p">))</span></span><a href="#l1729"></a>
<span id="l1730"></span><a href="#l1730"></a>
<span id="l1731">    <span class="k">def</span> <span class="nf">_parse_known_args</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg_strings</span><span class="p">,</span> <span class="n">namespace</span><span class="p">):</span></span><a href="#l1731"></a>
<span id="l1732">        <span class="c"># replace arg strings that are file references</span></span><a href="#l1732"></a>
<span id="l1733">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">fromfile_prefix_chars</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1733"></a>
<span id="l1734">            <span class="n">arg_strings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_read_args_from_files</span><span class="p">(</span><span class="n">arg_strings</span><span class="p">)</span></span><a href="#l1734"></a>
<span id="l1735"></span><a href="#l1735"></a>
<span id="l1736">        <span class="c"># map all mutually exclusive arguments to the other arguments</span></span><a href="#l1736"></a>
<span id="l1737">        <span class="c"># they can&#39;t occur with</span></span><a href="#l1737"></a>
<span id="l1738">        <span class="n">action_conflicts</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l1738"></a>
<span id="l1739">        <span class="k">for</span> <span class="n">mutex_group</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mutually_exclusive_groups</span><span class="p">:</span></span><a href="#l1739"></a>
<span id="l1740">            <span class="n">group_actions</span> <span class="o">=</span> <span class="n">mutex_group</span><span class="o">.</span><span class="n">_group_actions</span></span><a href="#l1740"></a>
<span id="l1741">            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">mutex_action</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">mutex_group</span><span class="o">.</span><span class="n">_group_actions</span><span class="p">):</span></span><a href="#l1741"></a>
<span id="l1742">                <span class="n">conflicts</span> <span class="o">=</span> <span class="n">action_conflicts</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">mutex_action</span><span class="p">,</span> <span class="p">[])</span></span><a href="#l1742"></a>
<span id="l1743">                <span class="n">conflicts</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">group_actions</span><span class="p">[:</span><span class="n">i</span><span class="p">])</span></span><a href="#l1743"></a>
<span id="l1744">                <span class="n">conflicts</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">group_actions</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">:])</span></span><a href="#l1744"></a>
<span id="l1745"></span><a href="#l1745"></a>
<span id="l1746">        <span class="c"># find all option indices, and determine the arg_string_pattern</span></span><a href="#l1746"></a>
<span id="l1747">        <span class="c"># which has an &#39;O&#39; if there is an option at an index,</span></span><a href="#l1747"></a>
<span id="l1748">        <span class="c"># an &#39;A&#39; if there is an argument, or a &#39;-&#39; if there is a &#39;--&#39;</span></span><a href="#l1748"></a>
<span id="l1749">        <span class="n">option_string_indices</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l1749"></a>
<span id="l1750">        <span class="n">arg_string_pattern_parts</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1750"></a>
<span id="l1751">        <span class="n">arg_strings_iter</span> <span class="o">=</span> <span class="nb">iter</span><span class="p">(</span><span class="n">arg_strings</span><span class="p">)</span></span><a href="#l1751"></a>
<span id="l1752">        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">arg_string</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">arg_strings_iter</span><span class="p">):</span></span><a href="#l1752"></a>
<span id="l1753"></span><a href="#l1753"></a>
<span id="l1754">            <span class="c"># all args after -- are non-options</span></span><a href="#l1754"></a>
<span id="l1755">            <span class="k">if</span> <span class="n">arg_string</span> <span class="o">==</span> <span class="s">&#39;--&#39;</span><span class="p">:</span></span><a href="#l1755"></a>
<span id="l1756">                <span class="n">arg_string_pattern_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;-&#39;</span><span class="p">)</span></span><a href="#l1756"></a>
<span id="l1757">                <span class="k">for</span> <span class="n">arg_string</span> <span class="ow">in</span> <span class="n">arg_strings_iter</span><span class="p">:</span></span><a href="#l1757"></a>
<span id="l1758">                    <span class="n">arg_string_pattern_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;A&#39;</span><span class="p">)</span></span><a href="#l1758"></a>
<span id="l1759"></span><a href="#l1759"></a>
<span id="l1760">            <span class="c"># otherwise, add the arg to the arg strings</span></span><a href="#l1760"></a>
<span id="l1761">            <span class="c"># and note the index if it was an option</span></span><a href="#l1761"></a>
<span id="l1762">            <span class="k">else</span><span class="p">:</span></span><a href="#l1762"></a>
<span id="l1763">                <span class="n">option_tuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_optional</span><span class="p">(</span><span class="n">arg_string</span><span class="p">)</span></span><a href="#l1763"></a>
<span id="l1764">                <span class="k">if</span> <span class="n">option_tuple</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1764"></a>
<span id="l1765">                    <span class="n">pattern</span> <span class="o">=</span> <span class="s">&#39;A&#39;</span></span><a href="#l1765"></a>
<span id="l1766">                <span class="k">else</span><span class="p">:</span></span><a href="#l1766"></a>
<span id="l1767">                    <span class="n">option_string_indices</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">option_tuple</span></span><a href="#l1767"></a>
<span id="l1768">                    <span class="n">pattern</span> <span class="o">=</span> <span class="s">&#39;O&#39;</span></span><a href="#l1768"></a>
<span id="l1769">                <span class="n">arg_string_pattern_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">pattern</span><span class="p">)</span></span><a href="#l1769"></a>
<span id="l1770"></span><a href="#l1770"></a>
<span id="l1771">        <span class="c"># join the pieces together to form the pattern</span></span><a href="#l1771"></a>
<span id="l1772">        <span class="n">arg_strings_pattern</span> <span class="o">=</span> <span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">arg_string_pattern_parts</span><span class="p">)</span></span><a href="#l1772"></a>
<span id="l1773"></span><a href="#l1773"></a>
<span id="l1774">        <span class="c"># converts arg strings to the appropriate and then takes the action</span></span><a href="#l1774"></a>
<span id="l1775">        <span class="n">seen_actions</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span></span><a href="#l1775"></a>
<span id="l1776">        <span class="n">seen_non_default_actions</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span></span><a href="#l1776"></a>
<span id="l1777"></span><a href="#l1777"></a>
<span id="l1778">        <span class="k">def</span> <span class="nf">take_action</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">argument_strings</span><span class="p">,</span> <span class="n">option_string</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1778"></a>
<span id="l1779">            <span class="n">seen_actions</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1779"></a>
<span id="l1780">            <span class="n">argument_values</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_values</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">argument_strings</span><span class="p">)</span></span><a href="#l1780"></a>
<span id="l1781"></span><a href="#l1781"></a>
<span id="l1782">            <span class="c"># error if this argument is not allowed with other previously</span></span><a href="#l1782"></a>
<span id="l1783">            <span class="c"># seen arguments, assuming that actions that use the default</span></span><a href="#l1783"></a>
<span id="l1784">            <span class="c"># value don&#39;t really count as &quot;present&quot;</span></span><a href="#l1784"></a>
<span id="l1785">            <span class="k">if</span> <span class="n">argument_values</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">action</span><span class="o">.</span><span class="n">default</span><span class="p">:</span></span><a href="#l1785"></a>
<span id="l1786">                <span class="n">seen_non_default_actions</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1786"></a>
<span id="l1787">                <span class="k">for</span> <span class="n">conflict_action</span> <span class="ow">in</span> <span class="n">action_conflicts</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="p">[]):</span></span><a href="#l1787"></a>
<span id="l1788">                    <span class="k">if</span> <span class="n">conflict_action</span> <span class="ow">in</span> <span class="n">seen_non_default_actions</span><span class="p">:</span></span><a href="#l1788"></a>
<span id="l1789">                        <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;not allowed with argument </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l1789"></a>
<span id="l1790">                        <span class="n">action_name</span> <span class="o">=</span> <span class="n">_get_action_name</span><span class="p">(</span><span class="n">conflict_action</span><span class="p">)</span></span><a href="#l1790"></a>
<span id="l1791">                        <span class="k">raise</span> <span class="n">ArgumentError</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">msg</span> <span class="o">%</span> <span class="n">action_name</span><span class="p">)</span></span><a href="#l1791"></a>
<span id="l1792"></span><a href="#l1792"></a>
<span id="l1793">            <span class="c"># take the action if we didn&#39;t receive a SUPPRESS value</span></span><a href="#l1793"></a>
<span id="l1794">            <span class="c"># (e.g. from a default)</span></span><a href="#l1794"></a>
<span id="l1795">            <span class="k">if</span> <span class="n">argument_values</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">SUPPRESS</span><span class="p">:</span></span><a href="#l1795"></a>
<span id="l1796">                <span class="n">action</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">namespace</span><span class="p">,</span> <span class="n">argument_values</span><span class="p">,</span> <span class="n">option_string</span><span class="p">)</span></span><a href="#l1796"></a>
<span id="l1797"></span><a href="#l1797"></a>
<span id="l1798">        <span class="c"># function to convert arg_strings into an optional action</span></span><a href="#l1798"></a>
<span id="l1799">        <span class="k">def</span> <span class="nf">consume_optional</span><span class="p">(</span><span class="n">start_index</span><span class="p">):</span></span><a href="#l1799"></a>
<span id="l1800"></span><a href="#l1800"></a>
<span id="l1801">            <span class="c"># get the optional identified at this index</span></span><a href="#l1801"></a>
<span id="l1802">            <span class="n">option_tuple</span> <span class="o">=</span> <span class="n">option_string_indices</span><span class="p">[</span><span class="n">start_index</span><span class="p">]</span></span><a href="#l1802"></a>
<span id="l1803">            <span class="n">action</span><span class="p">,</span> <span class="n">option_string</span><span class="p">,</span> <span class="n">explicit_arg</span> <span class="o">=</span> <span class="n">option_tuple</span></span><a href="#l1803"></a>
<span id="l1804"></span><a href="#l1804"></a>
<span id="l1805">            <span class="c"># identify additional optionals in the same arg string</span></span><a href="#l1805"></a>
<span id="l1806">            <span class="c"># (e.g. -xyz is the same as -x -y -z if no args are required)</span></span><a href="#l1806"></a>
<span id="l1807">            <span class="n">match_argument</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_match_argument</span></span><a href="#l1807"></a>
<span id="l1808">            <span class="n">action_tuples</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1808"></a>
<span id="l1809">            <span class="k">while</span> <span class="bp">True</span><span class="p">:</span></span><a href="#l1809"></a>
<span id="l1810"></span><a href="#l1810"></a>
<span id="l1811">                <span class="c"># if we found no optional action, skip it</span></span><a href="#l1811"></a>
<span id="l1812">                <span class="k">if</span> <span class="n">action</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1812"></a>
<span id="l1813">                    <span class="n">extras</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">arg_strings</span><span class="p">[</span><span class="n">start_index</span><span class="p">])</span></span><a href="#l1813"></a>
<span id="l1814">                    <span class="k">return</span> <span class="n">start_index</span> <span class="o">+</span> <span class="mi">1</span></span><a href="#l1814"></a>
<span id="l1815"></span><a href="#l1815"></a>
<span id="l1816">                <span class="c"># if there is an explicit argument, try to match the</span></span><a href="#l1816"></a>
<span id="l1817">                <span class="c"># optional&#39;s string arguments to only this</span></span><a href="#l1817"></a>
<span id="l1818">                <span class="k">if</span> <span class="n">explicit_arg</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1818"></a>
<span id="l1819">                    <span class="n">arg_count</span> <span class="o">=</span> <span class="n">match_argument</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="s">&#39;A&#39;</span><span class="p">)</span></span><a href="#l1819"></a>
<span id="l1820"></span><a href="#l1820"></a>
<span id="l1821">                    <span class="c"># if the action is a single-dash option and takes no</span></span><a href="#l1821"></a>
<span id="l1822">                    <span class="c"># arguments, try to parse more single-dash options out</span></span><a href="#l1822"></a>
<span id="l1823">                    <span class="c"># of the tail of the option string</span></span><a href="#l1823"></a>
<span id="l1824">                    <span class="n">chars</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">prefix_chars</span></span><a href="#l1824"></a>
<span id="l1825">                    <span class="k">if</span> <span class="n">arg_count</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">option_string</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">chars</span><span class="p">:</span></span><a href="#l1825"></a>
<span id="l1826">                        <span class="n">action_tuples</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">action</span><span class="p">,</span> <span class="p">[],</span> <span class="n">option_string</span><span class="p">))</span></span><a href="#l1826"></a>
<span id="l1827">                        <span class="n">char</span> <span class="o">=</span> <span class="n">option_string</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l1827"></a>
<span id="l1828">                        <span class="n">option_string</span> <span class="o">=</span> <span class="n">char</span> <span class="o">+</span> <span class="n">explicit_arg</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l1828"></a>
<span id="l1829">                        <span class="n">new_explicit_arg</span> <span class="o">=</span> <span class="n">explicit_arg</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span> <span class="ow">or</span> <span class="bp">None</span></span><a href="#l1829"></a>
<span id="l1830">                        <span class="n">optionals_map</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span></span><a href="#l1830"></a>
<span id="l1831">                        <span class="k">if</span> <span class="n">option_string</span> <span class="ow">in</span> <span class="n">optionals_map</span><span class="p">:</span></span><a href="#l1831"></a>
<span id="l1832">                            <span class="n">action</span> <span class="o">=</span> <span class="n">optionals_map</span><span class="p">[</span><span class="n">option_string</span><span class="p">]</span></span><a href="#l1832"></a>
<span id="l1833">                            <span class="n">explicit_arg</span> <span class="o">=</span> <span class="n">new_explicit_arg</span></span><a href="#l1833"></a>
<span id="l1834">                        <span class="k">else</span><span class="p">:</span></span><a href="#l1834"></a>
<span id="l1835">                            <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;ignored explicit argument </span><span class="si">%r</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l1835"></a>
<span id="l1836">                            <span class="k">raise</span> <span class="n">ArgumentError</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">msg</span> <span class="o">%</span> <span class="n">explicit_arg</span><span class="p">)</span></span><a href="#l1836"></a>
<span id="l1837"></span><a href="#l1837"></a>
<span id="l1838">                    <span class="c"># if the action expect exactly one argument, we&#39;ve</span></span><a href="#l1838"></a>
<span id="l1839">                    <span class="c"># successfully matched the option; exit the loop</span></span><a href="#l1839"></a>
<span id="l1840">                    <span class="k">elif</span> <span class="n">arg_count</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l1840"></a>
<span id="l1841">                        <span class="n">stop</span> <span class="o">=</span> <span class="n">start_index</span> <span class="o">+</span> <span class="mi">1</span></span><a href="#l1841"></a>
<span id="l1842">                        <span class="n">args</span> <span class="o">=</span> <span class="p">[</span><span class="n">explicit_arg</span><span class="p">]</span></span><a href="#l1842"></a>
<span id="l1843">                        <span class="n">action_tuples</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">action</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">option_string</span><span class="p">))</span></span><a href="#l1843"></a>
<span id="l1844">                        <span class="k">break</span></span><a href="#l1844"></a>
<span id="l1845"></span><a href="#l1845"></a>
<span id="l1846">                    <span class="c"># error if a double-dash option did not use the</span></span><a href="#l1846"></a>
<span id="l1847">                    <span class="c"># explicit argument</span></span><a href="#l1847"></a>
<span id="l1848">                    <span class="k">else</span><span class="p">:</span></span><a href="#l1848"></a>
<span id="l1849">                        <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;ignored explicit argument </span><span class="si">%r</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l1849"></a>
<span id="l1850">                        <span class="k">raise</span> <span class="n">ArgumentError</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">msg</span> <span class="o">%</span> <span class="n">explicit_arg</span><span class="p">)</span></span><a href="#l1850"></a>
<span id="l1851"></span><a href="#l1851"></a>
<span id="l1852">                <span class="c"># if there is no explicit argument, try to match the</span></span><a href="#l1852"></a>
<span id="l1853">                <span class="c"># optional&#39;s string arguments with the following strings</span></span><a href="#l1853"></a>
<span id="l1854">                <span class="c"># if successful, exit the loop</span></span><a href="#l1854"></a>
<span id="l1855">                <span class="k">else</span><span class="p">:</span></span><a href="#l1855"></a>
<span id="l1856">                    <span class="n">start</span> <span class="o">=</span> <span class="n">start_index</span> <span class="o">+</span> <span class="mi">1</span></span><a href="#l1856"></a>
<span id="l1857">                    <span class="n">selected_patterns</span> <span class="o">=</span> <span class="n">arg_strings_pattern</span><span class="p">[</span><span class="n">start</span><span class="p">:]</span></span><a href="#l1857"></a>
<span id="l1858">                    <span class="n">arg_count</span> <span class="o">=</span> <span class="n">match_argument</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">selected_patterns</span><span class="p">)</span></span><a href="#l1858"></a>
<span id="l1859">                    <span class="n">stop</span> <span class="o">=</span> <span class="n">start</span> <span class="o">+</span> <span class="n">arg_count</span></span><a href="#l1859"></a>
<span id="l1860">                    <span class="n">args</span> <span class="o">=</span> <span class="n">arg_strings</span><span class="p">[</span><span class="n">start</span><span class="p">:</span><span class="n">stop</span><span class="p">]</span></span><a href="#l1860"></a>
<span id="l1861">                    <span class="n">action_tuples</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">action</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">option_string</span><span class="p">))</span></span><a href="#l1861"></a>
<span id="l1862">                    <span class="k">break</span></span><a href="#l1862"></a>
<span id="l1863"></span><a href="#l1863"></a>
<span id="l1864">            <span class="c"># add the Optional to the list and return the index at which</span></span><a href="#l1864"></a>
<span id="l1865">            <span class="c"># the Optional&#39;s string args stopped</span></span><a href="#l1865"></a>
<span id="l1866">            <span class="k">assert</span> <span class="n">action_tuples</span></span><a href="#l1866"></a>
<span id="l1867">            <span class="k">for</span> <span class="n">action</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">option_string</span> <span class="ow">in</span> <span class="n">action_tuples</span><span class="p">:</span></span><a href="#l1867"></a>
<span id="l1868">                <span class="n">take_action</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">option_string</span><span class="p">)</span></span><a href="#l1868"></a>
<span id="l1869">            <span class="k">return</span> <span class="n">stop</span></span><a href="#l1869"></a>
<span id="l1870"></span><a href="#l1870"></a>
<span id="l1871">        <span class="c"># the list of Positionals left to be parsed; this is modified</span></span><a href="#l1871"></a>
<span id="l1872">        <span class="c"># by consume_positionals()</span></span><a href="#l1872"></a>
<span id="l1873">        <span class="n">positionals</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_positional_actions</span><span class="p">()</span></span><a href="#l1873"></a>
<span id="l1874"></span><a href="#l1874"></a>
<span id="l1875">        <span class="c"># function to convert arg_strings into positional actions</span></span><a href="#l1875"></a>
<span id="l1876">        <span class="k">def</span> <span class="nf">consume_positionals</span><span class="p">(</span><span class="n">start_index</span><span class="p">):</span></span><a href="#l1876"></a>
<span id="l1877">            <span class="c"># match as many Positionals as possible</span></span><a href="#l1877"></a>
<span id="l1878">            <span class="n">match_partial</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_match_arguments_partial</span></span><a href="#l1878"></a>
<span id="l1879">            <span class="n">selected_pattern</span> <span class="o">=</span> <span class="n">arg_strings_pattern</span><span class="p">[</span><span class="n">start_index</span><span class="p">:]</span></span><a href="#l1879"></a>
<span id="l1880">            <span class="n">arg_counts</span> <span class="o">=</span> <span class="n">match_partial</span><span class="p">(</span><span class="n">positionals</span><span class="p">,</span> <span class="n">selected_pattern</span><span class="p">)</span></span><a href="#l1880"></a>
<span id="l1881"></span><a href="#l1881"></a>
<span id="l1882">            <span class="c"># slice off the appropriate arg strings for each Positional</span></span><a href="#l1882"></a>
<span id="l1883">            <span class="c"># and add the Positional and its args to the list</span></span><a href="#l1883"></a>
<span id="l1884">            <span class="k">for</span> <span class="n">action</span><span class="p">,</span> <span class="n">arg_count</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">positionals</span><span class="p">,</span> <span class="n">arg_counts</span><span class="p">):</span></span><a href="#l1884"></a>
<span id="l1885">                <span class="n">args</span> <span class="o">=</span> <span class="n">arg_strings</span><span class="p">[</span><span class="n">start_index</span><span class="p">:</span> <span class="n">start_index</span> <span class="o">+</span> <span class="n">arg_count</span><span class="p">]</span></span><a href="#l1885"></a>
<span id="l1886">                <span class="n">start_index</span> <span class="o">+=</span> <span class="n">arg_count</span></span><a href="#l1886"></a>
<span id="l1887">                <span class="n">take_action</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">args</span><span class="p">)</span></span><a href="#l1887"></a>
<span id="l1888"></span><a href="#l1888"></a>
<span id="l1889">            <span class="c"># slice off the Positionals that we just parsed and return the</span></span><a href="#l1889"></a>
<span id="l1890">            <span class="c"># index at which the Positionals&#39; string args stopped</span></span><a href="#l1890"></a>
<span id="l1891">            <span class="n">positionals</span><span class="p">[:]</span> <span class="o">=</span> <span class="n">positionals</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">arg_counts</span><span class="p">):]</span></span><a href="#l1891"></a>
<span id="l1892">            <span class="k">return</span> <span class="n">start_index</span></span><a href="#l1892"></a>
<span id="l1893"></span><a href="#l1893"></a>
<span id="l1894">        <span class="c"># consume Positionals and Optionals alternately, until we have</span></span><a href="#l1894"></a>
<span id="l1895">        <span class="c"># passed the last option string</span></span><a href="#l1895"></a>
<span id="l1896">        <span class="n">extras</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1896"></a>
<span id="l1897">        <span class="n">start_index</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l1897"></a>
<span id="l1898">        <span class="k">if</span> <span class="n">option_string_indices</span><span class="p">:</span></span><a href="#l1898"></a>
<span id="l1899">            <span class="n">max_option_string_index</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">option_string_indices</span><span class="p">)</span></span><a href="#l1899"></a>
<span id="l1900">        <span class="k">else</span><span class="p">:</span></span><a href="#l1900"></a>
<span id="l1901">            <span class="n">max_option_string_index</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l1901"></a>
<span id="l1902">        <span class="k">while</span> <span class="n">start_index</span> <span class="o">&lt;=</span> <span class="n">max_option_string_index</span><span class="p">:</span></span><a href="#l1902"></a>
<span id="l1903"></span><a href="#l1903"></a>
<span id="l1904">            <span class="c"># consume any Positionals preceding the next option</span></span><a href="#l1904"></a>
<span id="l1905">            <span class="n">next_option_string_index</span> <span class="o">=</span> <span class="nb">min</span><span class="p">([</span></span><a href="#l1905"></a>
<span id="l1906">                <span class="n">index</span></span><a href="#l1906"></a>
<span id="l1907">                <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="n">option_string_indices</span></span><a href="#l1907"></a>
<span id="l1908">                <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="n">start_index</span><span class="p">])</span></span><a href="#l1908"></a>
<span id="l1909">            <span class="k">if</span> <span class="n">start_index</span> <span class="o">!=</span> <span class="n">next_option_string_index</span><span class="p">:</span></span><a href="#l1909"></a>
<span id="l1910">                <span class="n">positionals_end_index</span> <span class="o">=</span> <span class="n">consume_positionals</span><span class="p">(</span><span class="n">start_index</span><span class="p">)</span></span><a href="#l1910"></a>
<span id="l1911"></span><a href="#l1911"></a>
<span id="l1912">                <span class="c"># only try to parse the next optional if we didn&#39;t consume</span></span><a href="#l1912"></a>
<span id="l1913">                <span class="c"># the option string during the positionals parsing</span></span><a href="#l1913"></a>
<span id="l1914">                <span class="k">if</span> <span class="n">positionals_end_index</span> <span class="o">&gt;</span> <span class="n">start_index</span><span class="p">:</span></span><a href="#l1914"></a>
<span id="l1915">                    <span class="n">start_index</span> <span class="o">=</span> <span class="n">positionals_end_index</span></span><a href="#l1915"></a>
<span id="l1916">                    <span class="k">continue</span></span><a href="#l1916"></a>
<span id="l1917">                <span class="k">else</span><span class="p">:</span></span><a href="#l1917"></a>
<span id="l1918">                    <span class="n">start_index</span> <span class="o">=</span> <span class="n">positionals_end_index</span></span><a href="#l1918"></a>
<span id="l1919"></span><a href="#l1919"></a>
<span id="l1920">            <span class="c"># if we consumed all the positionals we could and we&#39;re not</span></span><a href="#l1920"></a>
<span id="l1921">            <span class="c"># at the index of an option string, there were extra arguments</span></span><a href="#l1921"></a>
<span id="l1922">            <span class="k">if</span> <span class="n">start_index</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">option_string_indices</span><span class="p">:</span></span><a href="#l1922"></a>
<span id="l1923">                <span class="n">strings</span> <span class="o">=</span> <span class="n">arg_strings</span><span class="p">[</span><span class="n">start_index</span><span class="p">:</span><span class="n">next_option_string_index</span><span class="p">]</span></span><a href="#l1923"></a>
<span id="l1924">                <span class="n">extras</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">strings</span><span class="p">)</span></span><a href="#l1924"></a>
<span id="l1925">                <span class="n">start_index</span> <span class="o">=</span> <span class="n">next_option_string_index</span></span><a href="#l1925"></a>
<span id="l1926"></span><a href="#l1926"></a>
<span id="l1927">            <span class="c"># consume the next optional and any arguments for it</span></span><a href="#l1927"></a>
<span id="l1928">            <span class="n">start_index</span> <span class="o">=</span> <span class="n">consume_optional</span><span class="p">(</span><span class="n">start_index</span><span class="p">)</span></span><a href="#l1928"></a>
<span id="l1929"></span><a href="#l1929"></a>
<span id="l1930">        <span class="c"># consume any positionals following the last Optional</span></span><a href="#l1930"></a>
<span id="l1931">        <span class="n">stop_index</span> <span class="o">=</span> <span class="n">consume_positionals</span><span class="p">(</span><span class="n">start_index</span><span class="p">)</span></span><a href="#l1931"></a>
<span id="l1932"></span><a href="#l1932"></a>
<span id="l1933">        <span class="c"># if we didn&#39;t consume all the argument strings, there were extras</span></span><a href="#l1933"></a>
<span id="l1934">        <span class="n">extras</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">arg_strings</span><span class="p">[</span><span class="n">stop_index</span><span class="p">:])</span></span><a href="#l1934"></a>
<span id="l1935"></span><a href="#l1935"></a>
<span id="l1936">        <span class="c"># if we didn&#39;t use all the Positional objects, there were too few</span></span><a href="#l1936"></a>
<span id="l1937">        <span class="c"># arg strings supplied.</span></span><a href="#l1937"></a>
<span id="l1938">        <span class="k">if</span> <span class="n">positionals</span><span class="p">:</span></span><a href="#l1938"></a>
<span id="l1939">            <span class="bp">self</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s">&#39;too few arguments&#39;</span><span class="p">))</span></span><a href="#l1939"></a>
<span id="l1940"></span><a href="#l1940"></a>
<span id="l1941">        <span class="c"># make sure all required actions were present, and convert defaults.</span></span><a href="#l1941"></a>
<span id="l1942">        <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_actions</span><span class="p">:</span></span><a href="#l1942"></a>
<span id="l1943">            <span class="k">if</span> <span class="n">action</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">seen_actions</span><span class="p">:</span></span><a href="#l1943"></a>
<span id="l1944">                <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">required</span><span class="p">:</span></span><a href="#l1944"></a>
<span id="l1945">                    <span class="n">name</span> <span class="o">=</span> <span class="n">_get_action_name</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1945"></a>
<span id="l1946">                    <span class="bp">self</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s">&#39;argument </span><span class="si">%s</span><span class="s"> is required&#39;</span><span class="p">)</span> <span class="o">%</span> <span class="n">name</span><span class="p">)</span></span><a href="#l1946"></a>
<span id="l1947">                <span class="k">else</span><span class="p">:</span></span><a href="#l1947"></a>
<span id="l1948">                    <span class="c"># Convert action default now instead of doing it before</span></span><a href="#l1948"></a>
<span id="l1949">                    <span class="c"># parsing arguments to avoid calling convert functions</span></span><a href="#l1949"></a>
<span id="l1950">                    <span class="c"># twice (which may fail) if the argument was given, but</span></span><a href="#l1950"></a>
<span id="l1951">                    <span class="c"># only if it was defined already in the namespace</span></span><a href="#l1951"></a>
<span id="l1952">                    <span class="k">if</span> <span class="p">(</span><span class="n">action</span><span class="o">.</span><span class="n">default</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span></span><a href="#l1952"></a>
<span id="l1953">                            <span class="nb">isinstance</span><span class="p">(</span><span class="n">action</span><span class="o">.</span><span class="n">default</span><span class="p">,</span> <span class="nb">basestring</span><span class="p">)</span> <span class="ow">and</span></span><a href="#l1953"></a>
<span id="l1954">                            <span class="nb">hasattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">dest</span><span class="p">)</span> <span class="ow">and</span></span><a href="#l1954"></a>
<span id="l1955">                            <span class="n">action</span><span class="o">.</span><span class="n">default</span> <span class="ow">is</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">dest</span><span class="p">)):</span></span><a href="#l1955"></a>
<span id="l1956">                        <span class="nb">setattr</span><span class="p">(</span><span class="n">namespace</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">dest</span><span class="p">,</span></span><a href="#l1956"></a>
<span id="l1957">                                <span class="bp">self</span><span class="o">.</span><span class="n">_get_value</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">default</span><span class="p">))</span></span><a href="#l1957"></a>
<span id="l1958"></span><a href="#l1958"></a>
<span id="l1959">        <span class="c"># make sure all required groups had one option present</span></span><a href="#l1959"></a>
<span id="l1960">        <span class="k">for</span> <span class="n">group</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mutually_exclusive_groups</span><span class="p">:</span></span><a href="#l1960"></a>
<span id="l1961">            <span class="k">if</span> <span class="n">group</span><span class="o">.</span><span class="n">required</span><span class="p">:</span></span><a href="#l1961"></a>
<span id="l1962">                <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">group</span><span class="o">.</span><span class="n">_group_actions</span><span class="p">:</span></span><a href="#l1962"></a>
<span id="l1963">                    <span class="k">if</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">seen_non_default_actions</span><span class="p">:</span></span><a href="#l1963"></a>
<span id="l1964">                        <span class="k">break</span></span><a href="#l1964"></a>
<span id="l1965"></span><a href="#l1965"></a>
<span id="l1966">                <span class="c"># if no actions were used, report the error</span></span><a href="#l1966"></a>
<span id="l1967">                <span class="k">else</span><span class="p">:</span></span><a href="#l1967"></a>
<span id="l1968">                    <span class="n">names</span> <span class="o">=</span> <span class="p">[</span><span class="n">_get_action_name</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l1968"></a>
<span id="l1969">                             <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">group</span><span class="o">.</span><span class="n">_group_actions</span></span><a href="#l1969"></a>
<span id="l1970">                             <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">help</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">SUPPRESS</span><span class="p">]</span></span><a href="#l1970"></a>
<span id="l1971">                    <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;one of the arguments </span><span class="si">%s</span><span class="s"> is required&#39;</span><span class="p">)</span></span><a href="#l1971"></a>
<span id="l1972">                    <span class="bp">self</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">msg</span> <span class="o">%</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">names</span><span class="p">))</span></span><a href="#l1972"></a>
<span id="l1973"></span><a href="#l1973"></a>
<span id="l1974">        <span class="c"># return the updated namespace and the extra arguments</span></span><a href="#l1974"></a>
<span id="l1975">        <span class="k">return</span> <span class="n">namespace</span><span class="p">,</span> <span class="n">extras</span></span><a href="#l1975"></a>
<span id="l1976"></span><a href="#l1976"></a>
<span id="l1977">    <span class="k">def</span> <span class="nf">_read_args_from_files</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg_strings</span><span class="p">):</span></span><a href="#l1977"></a>
<span id="l1978">        <span class="c"># expand arguments referencing files</span></span><a href="#l1978"></a>
<span id="l1979">        <span class="n">new_arg_strings</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1979"></a>
<span id="l1980">        <span class="k">for</span> <span class="n">arg_string</span> <span class="ow">in</span> <span class="n">arg_strings</span><span class="p">:</span></span><a href="#l1980"></a>
<span id="l1981"></span><a href="#l1981"></a>
<span id="l1982">            <span class="c"># for regular arguments, just add them back into the list</span></span><a href="#l1982"></a>
<span id="l1983">            <span class="k">if</span> <span class="ow">not</span> <span class="n">arg_string</span> <span class="ow">or</span> <span class="n">arg_string</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">fromfile_prefix_chars</span><span class="p">:</span></span><a href="#l1983"></a>
<span id="l1984">                <span class="n">new_arg_strings</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">arg_string</span><span class="p">)</span></span><a href="#l1984"></a>
<span id="l1985"></span><a href="#l1985"></a>
<span id="l1986">            <span class="c"># replace arguments referencing files with the file content</span></span><a href="#l1986"></a>
<span id="l1987">            <span class="k">else</span><span class="p">:</span></span><a href="#l1987"></a>
<span id="l1988">                <span class="k">try</span><span class="p">:</span></span><a href="#l1988"></a>
<span id="l1989">                    <span class="n">args_file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">arg_string</span><span class="p">[</span><span class="mi">1</span><span class="p">:])</span></span><a href="#l1989"></a>
<span id="l1990">                    <span class="k">try</span><span class="p">:</span></span><a href="#l1990"></a>
<span id="l1991">                        <span class="n">arg_strings</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1991"></a>
<span id="l1992">                        <span class="k">for</span> <span class="n">arg_line</span> <span class="ow">in</span> <span class="n">args_file</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">splitlines</span><span class="p">():</span></span><a href="#l1992"></a>
<span id="l1993">                            <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">convert_arg_line_to_args</span><span class="p">(</span><span class="n">arg_line</span><span class="p">):</span></span><a href="#l1993"></a>
<span id="l1994">                                <span class="n">arg_strings</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span></span><a href="#l1994"></a>
<span id="l1995">                        <span class="n">arg_strings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_read_args_from_files</span><span class="p">(</span><span class="n">arg_strings</span><span class="p">)</span></span><a href="#l1995"></a>
<span id="l1996">                        <span class="n">new_arg_strings</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">arg_strings</span><span class="p">)</span></span><a href="#l1996"></a>
<span id="l1997">                    <span class="k">finally</span><span class="p">:</span></span><a href="#l1997"></a>
<span id="l1998">                        <span class="n">args_file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></span><a href="#l1998"></a>
<span id="l1999">                <span class="k">except</span> <span class="ne">IOError</span><span class="p">:</span></span><a href="#l1999"></a>
<span id="l2000">                    <span class="n">err</span> <span class="o">=</span> <span class="n">_sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span></span><a href="#l2000"></a>
<span id="l2001">                    <span class="bp">self</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">err</span><span class="p">))</span></span><a href="#l2001"></a>
<span id="l2002"></span><a href="#l2002"></a>
<span id="l2003">        <span class="c"># return the modified argument list</span></span><a href="#l2003"></a>
<span id="l2004">        <span class="k">return</span> <span class="n">new_arg_strings</span></span><a href="#l2004"></a>
<span id="l2005"></span><a href="#l2005"></a>
<span id="l2006">    <span class="k">def</span> <span class="nf">convert_arg_line_to_args</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg_line</span><span class="p">):</span></span><a href="#l2006"></a>
<span id="l2007">        <span class="k">return</span> <span class="p">[</span><span class="n">arg_line</span><span class="p">]</span></span><a href="#l2007"></a>
<span id="l2008"></span><a href="#l2008"></a>
<span id="l2009">    <span class="k">def</span> <span class="nf">_match_argument</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">arg_strings_pattern</span><span class="p">):</span></span><a href="#l2009"></a>
<span id="l2010">        <span class="c"># match the pattern for this action to the arg strings</span></span><a href="#l2010"></a>
<span id="l2011">        <span class="n">nargs_pattern</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_nargs_pattern</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l2011"></a>
<span id="l2012">        <span class="n">match</span> <span class="o">=</span> <span class="n">_re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">nargs_pattern</span><span class="p">,</span> <span class="n">arg_strings_pattern</span><span class="p">)</span></span><a href="#l2012"></a>
<span id="l2013"></span><a href="#l2013"></a>
<span id="l2014">        <span class="c"># raise an exception if we weren&#39;t able to find a match</span></span><a href="#l2014"></a>
<span id="l2015">        <span class="k">if</span> <span class="n">match</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2015"></a>
<span id="l2016">            <span class="n">nargs_errors</span> <span class="o">=</span> <span class="p">{</span></span><a href="#l2016"></a>
<span id="l2017">                <span class="bp">None</span><span class="p">:</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;expected one argument&#39;</span><span class="p">),</span></span><a href="#l2017"></a>
<span id="l2018">                <span class="n">OPTIONAL</span><span class="p">:</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;expected at most one argument&#39;</span><span class="p">),</span></span><a href="#l2018"></a>
<span id="l2019">                <span class="n">ONE_OR_MORE</span><span class="p">:</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;expected at least one argument&#39;</span><span class="p">),</span></span><a href="#l2019"></a>
<span id="l2020">            <span class="p">}</span></span><a href="#l2020"></a>
<span id="l2021">            <span class="n">default</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;expected </span><span class="si">%s</span><span class="s"> argument(s)&#39;</span><span class="p">)</span> <span class="o">%</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span></span><a href="#l2021"></a>
<span id="l2022">            <span class="n">msg</span> <span class="o">=</span> <span class="n">nargs_errors</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">action</span><span class="o">.</span><span class="n">nargs</span><span class="p">,</span> <span class="n">default</span><span class="p">)</span></span><a href="#l2022"></a>
<span id="l2023">            <span class="k">raise</span> <span class="n">ArgumentError</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></span><a href="#l2023"></a>
<span id="l2024"></span><a href="#l2024"></a>
<span id="l2025">        <span class="c"># return the number of arguments matched</span></span><a href="#l2025"></a>
<span id="l2026">        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="n">match</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">))</span></span><a href="#l2026"></a>
<span id="l2027"></span><a href="#l2027"></a>
<span id="l2028">    <span class="k">def</span> <span class="nf">_match_arguments_partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">actions</span><span class="p">,</span> <span class="n">arg_strings_pattern</span><span class="p">):</span></span><a href="#l2028"></a>
<span id="l2029">        <span class="c"># progressively shorten the actions list by slicing off the</span></span><a href="#l2029"></a>
<span id="l2030">        <span class="c"># final actions until we find a match</span></span><a href="#l2030"></a>
<span id="l2031">        <span class="n">result</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l2031"></a>
<span id="l2032">        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">actions</span><span class="p">),</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">):</span></span><a href="#l2032"></a>
<span id="l2033">            <span class="n">actions_slice</span> <span class="o">=</span> <span class="n">actions</span><span class="p">[:</span><span class="n">i</span><span class="p">]</span></span><a href="#l2033"></a>
<span id="l2034">            <span class="n">pattern</span> <span class="o">=</span> <span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_nargs_pattern</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></span><a href="#l2034"></a>
<span id="l2035">                               <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">actions_slice</span><span class="p">])</span></span><a href="#l2035"></a>
<span id="l2036">            <span class="n">match</span> <span class="o">=</span> <span class="n">_re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">pattern</span><span class="p">,</span> <span class="n">arg_strings_pattern</span><span class="p">)</span></span><a href="#l2036"></a>
<span id="l2037">            <span class="k">if</span> <span class="n">match</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2037"></a>
<span id="l2038">                <span class="n">result</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="nb">len</span><span class="p">(</span><span class="n">string</span><span class="p">)</span> <span class="k">for</span> <span class="n">string</span> <span class="ow">in</span> <span class="n">match</span><span class="o">.</span><span class="n">groups</span><span class="p">()])</span></span><a href="#l2038"></a>
<span id="l2039">                <span class="k">break</span></span><a href="#l2039"></a>
<span id="l2040"></span><a href="#l2040"></a>
<span id="l2041">        <span class="c"># return the list of arg string counts</span></span><a href="#l2041"></a>
<span id="l2042">        <span class="k">return</span> <span class="n">result</span></span><a href="#l2042"></a>
<span id="l2043"></span><a href="#l2043"></a>
<span id="l2044">    <span class="k">def</span> <span class="nf">_parse_optional</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg_string</span><span class="p">):</span></span><a href="#l2044"></a>
<span id="l2045">        <span class="c"># if it&#39;s an empty string, it was meant to be a positional</span></span><a href="#l2045"></a>
<span id="l2046">        <span class="k">if</span> <span class="ow">not</span> <span class="n">arg_string</span><span class="p">:</span></span><a href="#l2046"></a>
<span id="l2047">            <span class="k">return</span> <span class="bp">None</span></span><a href="#l2047"></a>
<span id="l2048"></span><a href="#l2048"></a>
<span id="l2049">        <span class="c"># if it doesn&#39;t start with a prefix, it was meant to be positional</span></span><a href="#l2049"></a>
<span id="l2050">        <span class="k">if</span> <span class="ow">not</span> <span class="n">arg_string</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">prefix_chars</span><span class="p">:</span></span><a href="#l2050"></a>
<span id="l2051">            <span class="k">return</span> <span class="bp">None</span></span><a href="#l2051"></a>
<span id="l2052"></span><a href="#l2052"></a>
<span id="l2053">        <span class="c"># if the option string is present in the parser, return the action</span></span><a href="#l2053"></a>
<span id="l2054">        <span class="k">if</span> <span class="n">arg_string</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span><span class="p">:</span></span><a href="#l2054"></a>
<span id="l2055">            <span class="n">action</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span><span class="p">[</span><span class="n">arg_string</span><span class="p">]</span></span><a href="#l2055"></a>
<span id="l2056">            <span class="k">return</span> <span class="n">action</span><span class="p">,</span> <span class="n">arg_string</span><span class="p">,</span> <span class="bp">None</span></span><a href="#l2056"></a>
<span id="l2057"></span><a href="#l2057"></a>
<span id="l2058">        <span class="c"># if it&#39;s just a single character, it was meant to be positional</span></span><a href="#l2058"></a>
<span id="l2059">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arg_string</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l2059"></a>
<span id="l2060">            <span class="k">return</span> <span class="bp">None</span></span><a href="#l2060"></a>
<span id="l2061"></span><a href="#l2061"></a>
<span id="l2062">        <span class="c"># if the option string before the &quot;=&quot; is present, return the action</span></span><a href="#l2062"></a>
<span id="l2063">        <span class="k">if</span> <span class="s">&#39;=&#39;</span> <span class="ow">in</span> <span class="n">arg_string</span><span class="p">:</span></span><a href="#l2063"></a>
<span id="l2064">            <span class="n">option_string</span><span class="p">,</span> <span class="n">explicit_arg</span> <span class="o">=</span> <span class="n">arg_string</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;=&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></span><a href="#l2064"></a>
<span id="l2065">            <span class="k">if</span> <span class="n">option_string</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span><span class="p">:</span></span><a href="#l2065"></a>
<span id="l2066">                <span class="n">action</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span><span class="p">[</span><span class="n">option_string</span><span class="p">]</span></span><a href="#l2066"></a>
<span id="l2067">                <span class="k">return</span> <span class="n">action</span><span class="p">,</span> <span class="n">option_string</span><span class="p">,</span> <span class="n">explicit_arg</span></span><a href="#l2067"></a>
<span id="l2068"></span><a href="#l2068"></a>
<span id="l2069">        <span class="c"># search through all possible prefixes of the option string</span></span><a href="#l2069"></a>
<span id="l2070">        <span class="c"># and all actions in the parser for possible interpretations</span></span><a href="#l2070"></a>
<span id="l2071">        <span class="n">option_tuples</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_option_tuples</span><span class="p">(</span><span class="n">arg_string</span><span class="p">)</span></span><a href="#l2071"></a>
<span id="l2072"></span><a href="#l2072"></a>
<span id="l2073">        <span class="c"># if multiple actions match, the option string was ambiguous</span></span><a href="#l2073"></a>
<span id="l2074">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">option_tuples</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l2074"></a>
<span id="l2075">            <span class="n">options</span> <span class="o">=</span> <span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">option_string</span></span><a href="#l2075"></a>
<span id="l2076">                <span class="k">for</span> <span class="n">action</span><span class="p">,</span> <span class="n">option_string</span><span class="p">,</span> <span class="n">explicit_arg</span> <span class="ow">in</span> <span class="n">option_tuples</span><span class="p">])</span></span><a href="#l2076"></a>
<span id="l2077">            <span class="n">tup</span> <span class="o">=</span> <span class="n">arg_string</span><span class="p">,</span> <span class="n">options</span></span><a href="#l2077"></a>
<span id="l2078">            <span class="bp">self</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s">&#39;ambiguous option: </span><span class="si">%s</span><span class="s"> could match </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">)</span> <span class="o">%</span> <span class="n">tup</span><span class="p">)</span></span><a href="#l2078"></a>
<span id="l2079"></span><a href="#l2079"></a>
<span id="l2080">        <span class="c"># if exactly one action matched, this segmentation is good,</span></span><a href="#l2080"></a>
<span id="l2081">        <span class="c"># so return the parsed action</span></span><a href="#l2081"></a>
<span id="l2082">        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">option_tuples</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l2082"></a>
<span id="l2083">            <span class="n">option_tuple</span><span class="p">,</span> <span class="o">=</span> <span class="n">option_tuples</span></span><a href="#l2083"></a>
<span id="l2084">            <span class="k">return</span> <span class="n">option_tuple</span></span><a href="#l2084"></a>
<span id="l2085"></span><a href="#l2085"></a>
<span id="l2086">        <span class="c"># if it was not found as an option, but it looks like a negative</span></span><a href="#l2086"></a>
<span id="l2087">        <span class="c"># number, it was meant to be positional</span></span><a href="#l2087"></a>
<span id="l2088">        <span class="c"># unless there are negative-number-like options</span></span><a href="#l2088"></a>
<span id="l2089">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_negative_number_matcher</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">arg_string</span><span class="p">):</span></span><a href="#l2089"></a>
<span id="l2090">            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_has_negative_number_optionals</span><span class="p">:</span></span><a href="#l2090"></a>
<span id="l2091">                <span class="k">return</span> <span class="bp">None</span></span><a href="#l2091"></a>
<span id="l2092"></span><a href="#l2092"></a>
<span id="l2093">        <span class="c"># if it contains a space, it was meant to be a positional</span></span><a href="#l2093"></a>
<span id="l2094">        <span class="k">if</span> <span class="s">&#39; &#39;</span> <span class="ow">in</span> <span class="n">arg_string</span><span class="p">:</span></span><a href="#l2094"></a>
<span id="l2095">            <span class="k">return</span> <span class="bp">None</span></span><a href="#l2095"></a>
<span id="l2096"></span><a href="#l2096"></a>
<span id="l2097">        <span class="c"># it was meant to be an optional but there is no such option</span></span><a href="#l2097"></a>
<span id="l2098">        <span class="c"># in this parser (though it might be a valid option in a subparser)</span></span><a href="#l2098"></a>
<span id="l2099">        <span class="k">return</span> <span class="bp">None</span><span class="p">,</span> <span class="n">arg_string</span><span class="p">,</span> <span class="bp">None</span></span><a href="#l2099"></a>
<span id="l2100"></span><a href="#l2100"></a>
<span id="l2101">    <span class="k">def</span> <span class="nf">_get_option_tuples</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">option_string</span><span class="p">):</span></span><a href="#l2101"></a>
<span id="l2102">        <span class="n">result</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l2102"></a>
<span id="l2103"></span><a href="#l2103"></a>
<span id="l2104">        <span class="c"># option strings starting with two prefix characters are only</span></span><a href="#l2104"></a>
<span id="l2105">        <span class="c"># split at the &#39;=&#39;</span></span><a href="#l2105"></a>
<span id="l2106">        <span class="n">chars</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">prefix_chars</span></span><a href="#l2106"></a>
<span id="l2107">        <span class="k">if</span> <span class="n">option_string</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="ow">in</span> <span class="n">chars</span> <span class="ow">and</span> <span class="n">option_string</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="ow">in</span> <span class="n">chars</span><span class="p">:</span></span><a href="#l2107"></a>
<span id="l2108">            <span class="k">if</span> <span class="s">&#39;=&#39;</span> <span class="ow">in</span> <span class="n">option_string</span><span class="p">:</span></span><a href="#l2108"></a>
<span id="l2109">                <span class="n">option_prefix</span><span class="p">,</span> <span class="n">explicit_arg</span> <span class="o">=</span> <span class="n">option_string</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;=&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></span><a href="#l2109"></a>
<span id="l2110">            <span class="k">else</span><span class="p">:</span></span><a href="#l2110"></a>
<span id="l2111">                <span class="n">option_prefix</span> <span class="o">=</span> <span class="n">option_string</span></span><a href="#l2111"></a>
<span id="l2112">                <span class="n">explicit_arg</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l2112"></a>
<span id="l2113">            <span class="k">for</span> <span class="n">option_string</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span><span class="p">:</span></span><a href="#l2113"></a>
<span id="l2114">                <span class="k">if</span> <span class="n">option_string</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">option_prefix</span><span class="p">):</span></span><a href="#l2114"></a>
<span id="l2115">                    <span class="n">action</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span><span class="p">[</span><span class="n">option_string</span><span class="p">]</span></span><a href="#l2115"></a>
<span id="l2116">                    <span class="n">tup</span> <span class="o">=</span> <span class="n">action</span><span class="p">,</span> <span class="n">option_string</span><span class="p">,</span> <span class="n">explicit_arg</span></span><a href="#l2116"></a>
<span id="l2117">                    <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tup</span><span class="p">)</span></span><a href="#l2117"></a>
<span id="l2118"></span><a href="#l2118"></a>
<span id="l2119">        <span class="c"># single character options can be concatenated with their arguments</span></span><a href="#l2119"></a>
<span id="l2120">        <span class="c"># but multiple character options always have to have their argument</span></span><a href="#l2120"></a>
<span id="l2121">        <span class="c"># separate</span></span><a href="#l2121"></a>
<span id="l2122">        <span class="k">elif</span> <span class="n">option_string</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="ow">in</span> <span class="n">chars</span> <span class="ow">and</span> <span class="n">option_string</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">chars</span><span class="p">:</span></span><a href="#l2122"></a>
<span id="l2123">            <span class="n">option_prefix</span> <span class="o">=</span> <span class="n">option_string</span></span><a href="#l2123"></a>
<span id="l2124">            <span class="n">explicit_arg</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l2124"></a>
<span id="l2125">            <span class="n">short_option_prefix</span> <span class="o">=</span> <span class="n">option_string</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span></span><a href="#l2125"></a>
<span id="l2126">            <span class="n">short_explicit_arg</span> <span class="o">=</span> <span class="n">option_string</span><span class="p">[</span><span class="mi">2</span><span class="p">:]</span></span><a href="#l2126"></a>
<span id="l2127"></span><a href="#l2127"></a>
<span id="l2128">            <span class="k">for</span> <span class="n">option_string</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span><span class="p">:</span></span><a href="#l2128"></a>
<span id="l2129">                <span class="k">if</span> <span class="n">option_string</span> <span class="o">==</span> <span class="n">short_option_prefix</span><span class="p">:</span></span><a href="#l2129"></a>
<span id="l2130">                    <span class="n">action</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span><span class="p">[</span><span class="n">option_string</span><span class="p">]</span></span><a href="#l2130"></a>
<span id="l2131">                    <span class="n">tup</span> <span class="o">=</span> <span class="n">action</span><span class="p">,</span> <span class="n">option_string</span><span class="p">,</span> <span class="n">short_explicit_arg</span></span><a href="#l2131"></a>
<span id="l2132">                    <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tup</span><span class="p">)</span></span><a href="#l2132"></a>
<span id="l2133">                <span class="k">elif</span> <span class="n">option_string</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">option_prefix</span><span class="p">):</span></span><a href="#l2133"></a>
<span id="l2134">                    <span class="n">action</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_option_string_actions</span><span class="p">[</span><span class="n">option_string</span><span class="p">]</span></span><a href="#l2134"></a>
<span id="l2135">                    <span class="n">tup</span> <span class="o">=</span> <span class="n">action</span><span class="p">,</span> <span class="n">option_string</span><span class="p">,</span> <span class="n">explicit_arg</span></span><a href="#l2135"></a>
<span id="l2136">                    <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tup</span><span class="p">)</span></span><a href="#l2136"></a>
<span id="l2137"></span><a href="#l2137"></a>
<span id="l2138">        <span class="c"># shouldn&#39;t ever get here</span></span><a href="#l2138"></a>
<span id="l2139">        <span class="k">else</span><span class="p">:</span></span><a href="#l2139"></a>
<span id="l2140">            <span class="bp">self</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s">&#39;unexpected option string: </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">)</span> <span class="o">%</span> <span class="n">option_string</span><span class="p">)</span></span><a href="#l2140"></a>
<span id="l2141"></span><a href="#l2141"></a>
<span id="l2142">        <span class="c"># return the collected option tuples</span></span><a href="#l2142"></a>
<span id="l2143">        <span class="k">return</span> <span class="n">result</span></span><a href="#l2143"></a>
<span id="l2144"></span><a href="#l2144"></a>
<span id="l2145">    <span class="k">def</span> <span class="nf">_get_nargs_pattern</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></span><a href="#l2145"></a>
<span id="l2146">        <span class="c"># in all examples below, we have to allow for &#39;--&#39; args</span></span><a href="#l2146"></a>
<span id="l2147">        <span class="c"># which are represented as &#39;-&#39; in the pattern</span></span><a href="#l2147"></a>
<span id="l2148">        <span class="n">nargs</span> <span class="o">=</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span></span><a href="#l2148"></a>
<span id="l2149"></span><a href="#l2149"></a>
<span id="l2150">        <span class="c"># the default (None) is assumed to be a single argument</span></span><a href="#l2150"></a>
<span id="l2151">        <span class="k">if</span> <span class="n">nargs</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2151"></a>
<span id="l2152">            <span class="n">nargs_pattern</span> <span class="o">=</span> <span class="s">&#39;(-*A-*)&#39;</span></span><a href="#l2152"></a>
<span id="l2153"></span><a href="#l2153"></a>
<span id="l2154">        <span class="c"># allow zero or one arguments</span></span><a href="#l2154"></a>
<span id="l2155">        <span class="k">elif</span> <span class="n">nargs</span> <span class="o">==</span> <span class="n">OPTIONAL</span><span class="p">:</span></span><a href="#l2155"></a>
<span id="l2156">            <span class="n">nargs_pattern</span> <span class="o">=</span> <span class="s">&#39;(-*A?-*)&#39;</span></span><a href="#l2156"></a>
<span id="l2157"></span><a href="#l2157"></a>
<span id="l2158">        <span class="c"># allow zero or more arguments</span></span><a href="#l2158"></a>
<span id="l2159">        <span class="k">elif</span> <span class="n">nargs</span> <span class="o">==</span> <span class="n">ZERO_OR_MORE</span><span class="p">:</span></span><a href="#l2159"></a>
<span id="l2160">            <span class="n">nargs_pattern</span> <span class="o">=</span> <span class="s">&#39;(-*[A-]*)&#39;</span></span><a href="#l2160"></a>
<span id="l2161"></span><a href="#l2161"></a>
<span id="l2162">        <span class="c"># allow one or more arguments</span></span><a href="#l2162"></a>
<span id="l2163">        <span class="k">elif</span> <span class="n">nargs</span> <span class="o">==</span> <span class="n">ONE_OR_MORE</span><span class="p">:</span></span><a href="#l2163"></a>
<span id="l2164">            <span class="n">nargs_pattern</span> <span class="o">=</span> <span class="s">&#39;(-*A[A-]*)&#39;</span></span><a href="#l2164"></a>
<span id="l2165"></span><a href="#l2165"></a>
<span id="l2166">        <span class="c"># allow any number of options or arguments</span></span><a href="#l2166"></a>
<span id="l2167">        <span class="k">elif</span> <span class="n">nargs</span> <span class="o">==</span> <span class="n">REMAINDER</span><span class="p">:</span></span><a href="#l2167"></a>
<span id="l2168">            <span class="n">nargs_pattern</span> <span class="o">=</span> <span class="s">&#39;([-AO]*)&#39;</span></span><a href="#l2168"></a>
<span id="l2169"></span><a href="#l2169"></a>
<span id="l2170">        <span class="c"># allow one argument followed by any number of options or arguments</span></span><a href="#l2170"></a>
<span id="l2171">        <span class="k">elif</span> <span class="n">nargs</span> <span class="o">==</span> <span class="n">PARSER</span><span class="p">:</span></span><a href="#l2171"></a>
<span id="l2172">            <span class="n">nargs_pattern</span> <span class="o">=</span> <span class="s">&#39;(-*A[-AO]*)&#39;</span></span><a href="#l2172"></a>
<span id="l2173"></span><a href="#l2173"></a>
<span id="l2174">        <span class="c"># all others should be integers</span></span><a href="#l2174"></a>
<span id="l2175">        <span class="k">else</span><span class="p">:</span></span><a href="#l2175"></a>
<span id="l2176">            <span class="n">nargs_pattern</span> <span class="o">=</span> <span class="s">&#39;(-*</span><span class="si">%s</span><span class="s">-*)&#39;</span> <span class="o">%</span> <span class="s">&#39;-*&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s">&#39;A&#39;</span> <span class="o">*</span> <span class="n">nargs</span><span class="p">)</span></span><a href="#l2176"></a>
<span id="l2177"></span><a href="#l2177"></a>
<span id="l2178">        <span class="c"># if this is an optional action, -- is not allowed</span></span><a href="#l2178"></a>
<span id="l2179">        <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">:</span></span><a href="#l2179"></a>
<span id="l2180">            <span class="n">nargs_pattern</span> <span class="o">=</span> <span class="n">nargs_pattern</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;-*&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)</span></span><a href="#l2180"></a>
<span id="l2181">            <span class="n">nargs_pattern</span> <span class="o">=</span> <span class="n">nargs_pattern</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;-&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)</span></span><a href="#l2181"></a>
<span id="l2182"></span><a href="#l2182"></a>
<span id="l2183">        <span class="c"># return the pattern</span></span><a href="#l2183"></a>
<span id="l2184">        <span class="k">return</span> <span class="n">nargs_pattern</span></span><a href="#l2184"></a>
<span id="l2185"></span><a href="#l2185"></a>
<span id="l2186">    <span class="c"># ========================</span></span><a href="#l2186"></a>
<span id="l2187">    <span class="c"># Value conversion methods</span></span><a href="#l2187"></a>
<span id="l2188">    <span class="c"># ========================</span></span><a href="#l2188"></a>
<span id="l2189">    <span class="k">def</span> <span class="nf">_get_values</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">arg_strings</span><span class="p">):</span></span><a href="#l2189"></a>
<span id="l2190">        <span class="c"># for everything but PARSER, REMAINDER args, strip out first &#39;--&#39;</span></span><a href="#l2190"></a>
<span id="l2191">        <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">[</span><span class="n">PARSER</span><span class="p">,</span> <span class="n">REMAINDER</span><span class="p">]:</span></span><a href="#l2191"></a>
<span id="l2192">            <span class="k">try</span><span class="p">:</span></span><a href="#l2192"></a>
<span id="l2193">                <span class="n">arg_strings</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="s">&#39;--&#39;</span><span class="p">)</span></span><a href="#l2193"></a>
<span id="l2194">            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span></span><a href="#l2194"></a>
<span id="l2195">                <span class="k">pass</span></span><a href="#l2195"></a>
<span id="l2196"></span><a href="#l2196"></a>
<span id="l2197">        <span class="c"># optional argument produces a default when not present</span></span><a href="#l2197"></a>
<span id="l2198">        <span class="k">if</span> <span class="ow">not</span> <span class="n">arg_strings</span> <span class="ow">and</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="o">==</span> <span class="n">OPTIONAL</span><span class="p">:</span></span><a href="#l2198"></a>
<span id="l2199">            <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">:</span></span><a href="#l2199"></a>
<span id="l2200">                <span class="n">value</span> <span class="o">=</span> <span class="n">action</span><span class="o">.</span><span class="n">const</span></span><a href="#l2200"></a>
<span id="l2201">            <span class="k">else</span><span class="p">:</span></span><a href="#l2201"></a>
<span id="l2202">                <span class="n">value</span> <span class="o">=</span> <span class="n">action</span><span class="o">.</span><span class="n">default</span></span><a href="#l2202"></a>
<span id="l2203">            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">basestring</span><span class="p">):</span></span><a href="#l2203"></a>
<span id="l2204">                <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_value</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span></span><a href="#l2204"></a>
<span id="l2205">                <span class="bp">self</span><span class="o">.</span><span class="n">_check_value</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span></span><a href="#l2205"></a>
<span id="l2206"></span><a href="#l2206"></a>
<span id="l2207">        <span class="c"># when nargs=&#39;*&#39; on a positional, if there were no command-line</span></span><a href="#l2207"></a>
<span id="l2208">        <span class="c"># args, use the default if it is anything other than None</span></span><a href="#l2208"></a>
<span id="l2209">        <span class="k">elif</span> <span class="p">(</span><span class="ow">not</span> <span class="n">arg_strings</span> <span class="ow">and</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="o">==</span> <span class="n">ZERO_OR_MORE</span> <span class="ow">and</span></span><a href="#l2209"></a>
<span id="l2210">              <span class="ow">not</span> <span class="n">action</span><span class="o">.</span><span class="n">option_strings</span><span class="p">):</span></span><a href="#l2210"></a>
<span id="l2211">            <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">default</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2211"></a>
<span id="l2212">                <span class="n">value</span> <span class="o">=</span> <span class="n">action</span><span class="o">.</span><span class="n">default</span></span><a href="#l2212"></a>
<span id="l2213">            <span class="k">else</span><span class="p">:</span></span><a href="#l2213"></a>
<span id="l2214">                <span class="n">value</span> <span class="o">=</span> <span class="n">arg_strings</span></span><a href="#l2214"></a>
<span id="l2215">            <span class="bp">self</span><span class="o">.</span><span class="n">_check_value</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span></span><a href="#l2215"></a>
<span id="l2216"></span><a href="#l2216"></a>
<span id="l2217">        <span class="c"># single argument or optional argument produces a single value</span></span><a href="#l2217"></a>
<span id="l2218">        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">arg_strings</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span> <span class="ow">and</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="ow">in</span> <span class="p">[</span><span class="bp">None</span><span class="p">,</span> <span class="n">OPTIONAL</span><span class="p">]:</span></span><a href="#l2218"></a>
<span id="l2219">            <span class="n">arg_string</span><span class="p">,</span> <span class="o">=</span> <span class="n">arg_strings</span></span><a href="#l2219"></a>
<span id="l2220">            <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_value</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">arg_string</span><span class="p">)</span></span><a href="#l2220"></a>
<span id="l2221">            <span class="bp">self</span><span class="o">.</span><span class="n">_check_value</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span></span><a href="#l2221"></a>
<span id="l2222"></span><a href="#l2222"></a>
<span id="l2223">        <span class="c"># REMAINDER arguments convert all values, checking none</span></span><a href="#l2223"></a>
<span id="l2224">        <span class="k">elif</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="o">==</span> <span class="n">REMAINDER</span><span class="p">:</span></span><a href="#l2224"></a>
<span id="l2225">            <span class="n">value</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_value</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">arg_strings</span><span class="p">]</span></span><a href="#l2225"></a>
<span id="l2226"></span><a href="#l2226"></a>
<span id="l2227">        <span class="c"># PARSER arguments convert all values, but check only the first</span></span><a href="#l2227"></a>
<span id="l2228">        <span class="k">elif</span> <span class="n">action</span><span class="o">.</span><span class="n">nargs</span> <span class="o">==</span> <span class="n">PARSER</span><span class="p">:</span></span><a href="#l2228"></a>
<span id="l2229">            <span class="n">value</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_value</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">arg_strings</span><span class="p">]</span></span><a href="#l2229"></a>
<span id="l2230">            <span class="bp">self</span><span class="o">.</span><span class="n">_check_value</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">value</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span></span><a href="#l2230"></a>
<span id="l2231"></span><a href="#l2231"></a>
<span id="l2232">        <span class="c"># all other types of nargs produce a list</span></span><a href="#l2232"></a>
<span id="l2233">        <span class="k">else</span><span class="p">:</span></span><a href="#l2233"></a>
<span id="l2234">            <span class="n">value</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_value</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">arg_strings</span><span class="p">]</span></span><a href="#l2234"></a>
<span id="l2235">            <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">value</span><span class="p">:</span></span><a href="#l2235"></a>
<span id="l2236">                <span class="bp">self</span><span class="o">.</span><span class="n">_check_value</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">v</span><span class="p">)</span></span><a href="#l2236"></a>
<span id="l2237"></span><a href="#l2237"></a>
<span id="l2238">        <span class="c"># return the converted value</span></span><a href="#l2238"></a>
<span id="l2239">        <span class="k">return</span> <span class="n">value</span></span><a href="#l2239"></a>
<span id="l2240"></span><a href="#l2240"></a>
<span id="l2241">    <span class="k">def</span> <span class="nf">_get_value</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">arg_string</span><span class="p">):</span></span><a href="#l2241"></a>
<span id="l2242">        <span class="n">type_func</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_registry_get</span><span class="p">(</span><span class="s">&#39;type&#39;</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">type</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">type</span><span class="p">)</span></span><a href="#l2242"></a>
<span id="l2243">        <span class="k">if</span> <span class="ow">not</span> <span class="n">_callable</span><span class="p">(</span><span class="n">type_func</span><span class="p">):</span></span><a href="#l2243"></a>
<span id="l2244">            <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%r</span><span class="s"> is not callable&#39;</span><span class="p">)</span></span><a href="#l2244"></a>
<span id="l2245">            <span class="k">raise</span> <span class="n">ArgumentError</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">msg</span> <span class="o">%</span> <span class="n">type_func</span><span class="p">)</span></span><a href="#l2245"></a>
<span id="l2246"></span><a href="#l2246"></a>
<span id="l2247">        <span class="c"># convert the value to the appropriate type</span></span><a href="#l2247"></a>
<span id="l2248">        <span class="k">try</span><span class="p">:</span></span><a href="#l2248"></a>
<span id="l2249">            <span class="n">result</span> <span class="o">=</span> <span class="n">type_func</span><span class="p">(</span><span class="n">arg_string</span><span class="p">)</span></span><a href="#l2249"></a>
<span id="l2250"></span><a href="#l2250"></a>
<span id="l2251">        <span class="c"># ArgumentTypeErrors indicate errors</span></span><a href="#l2251"></a>
<span id="l2252">        <span class="k">except</span> <span class="n">ArgumentTypeError</span><span class="p">:</span></span><a href="#l2252"></a>
<span id="l2253">            <span class="n">name</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">action</span><span class="o">.</span><span class="n">type</span><span class="p">,</span> <span class="s">&#39;__name__&#39;</span><span class="p">,</span> <span class="nb">repr</span><span class="p">(</span><span class="n">action</span><span class="o">.</span><span class="n">type</span><span class="p">))</span></span><a href="#l2253"></a>
<span id="l2254">            <span class="n">msg</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">_sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()[</span><span class="mi">1</span><span class="p">])</span></span><a href="#l2254"></a>
<span id="l2255">            <span class="k">raise</span> <span class="n">ArgumentError</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></span><a href="#l2255"></a>
<span id="l2256"></span><a href="#l2256"></a>
<span id="l2257">        <span class="c"># TypeErrors or ValueErrors also indicate errors</span></span><a href="#l2257"></a>
<span id="l2258">        <span class="k">except</span> <span class="p">(</span><span class="ne">TypeError</span><span class="p">,</span> <span class="ne">ValueError</span><span class="p">):</span></span><a href="#l2258"></a>
<span id="l2259">            <span class="n">name</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">action</span><span class="o">.</span><span class="n">type</span><span class="p">,</span> <span class="s">&#39;__name__&#39;</span><span class="p">,</span> <span class="nb">repr</span><span class="p">(</span><span class="n">action</span><span class="o">.</span><span class="n">type</span><span class="p">))</span></span><a href="#l2259"></a>
<span id="l2260">            <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;invalid </span><span class="si">%s</span><span class="s"> value: </span><span class="si">%r</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l2260"></a>
<span id="l2261">            <span class="k">raise</span> <span class="n">ArgumentError</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">msg</span> <span class="o">%</span> <span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">arg_string</span><span class="p">))</span></span><a href="#l2261"></a>
<span id="l2262"></span><a href="#l2262"></a>
<span id="l2263">        <span class="c"># return the converted value</span></span><a href="#l2263"></a>
<span id="l2264">        <span class="k">return</span> <span class="n">result</span></span><a href="#l2264"></a>
<span id="l2265"></span><a href="#l2265"></a>
<span id="l2266">    <span class="k">def</span> <span class="nf">_check_value</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span></span><a href="#l2266"></a>
<span id="l2267">        <span class="c"># converted value must be one of the choices (if specified)</span></span><a href="#l2267"></a>
<span id="l2268">        <span class="k">if</span> <span class="n">action</span><span class="o">.</span><span class="n">choices</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="n">value</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">action</span><span class="o">.</span><span class="n">choices</span><span class="p">:</span></span><a href="#l2268"></a>
<span id="l2269">            <span class="n">tup</span> <span class="o">=</span> <span class="n">value</span><span class="p">,</span> <span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="nb">repr</span><span class="p">,</span> <span class="n">action</span><span class="o">.</span><span class="n">choices</span><span class="p">))</span></span><a href="#l2269"></a>
<span id="l2270">            <span class="n">msg</span> <span class="o">=</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;invalid choice: </span><span class="si">%r</span><span class="s"> (choose from </span><span class="si">%s</span><span class="s">)&#39;</span><span class="p">)</span> <span class="o">%</span> <span class="n">tup</span></span><a href="#l2270"></a>
<span id="l2271">            <span class="k">raise</span> <span class="n">ArgumentError</span><span class="p">(</span><span class="n">action</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></span><a href="#l2271"></a>
<span id="l2272"></span><a href="#l2272"></a>
<span id="l2273">    <span class="c"># =======================</span></span><a href="#l2273"></a>
<span id="l2274">    <span class="c"># Help-formatting methods</span></span><a href="#l2274"></a>
<span id="l2275">    <span class="c"># =======================</span></span><a href="#l2275"></a>
<span id="l2276">    <span class="k">def</span> <span class="nf">format_usage</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2276"></a>
<span id="l2277">        <span class="n">formatter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_formatter</span><span class="p">()</span></span><a href="#l2277"></a>
<span id="l2278">        <span class="n">formatter</span><span class="o">.</span><span class="n">add_usage</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">usage</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_actions</span><span class="p">,</span></span><a href="#l2278"></a>
<span id="l2279">                            <span class="bp">self</span><span class="o">.</span><span class="n">_mutually_exclusive_groups</span><span class="p">)</span></span><a href="#l2279"></a>
<span id="l2280">        <span class="k">return</span> <span class="n">formatter</span><span class="o">.</span><span class="n">format_help</span><span class="p">()</span></span><a href="#l2280"></a>
<span id="l2281"></span><a href="#l2281"></a>
<span id="l2282">    <span class="k">def</span> <span class="nf">format_help</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2282"></a>
<span id="l2283">        <span class="n">formatter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_formatter</span><span class="p">()</span></span><a href="#l2283"></a>
<span id="l2284"></span><a href="#l2284"></a>
<span id="l2285">        <span class="c"># usage</span></span><a href="#l2285"></a>
<span id="l2286">        <span class="n">formatter</span><span class="o">.</span><span class="n">add_usage</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">usage</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_actions</span><span class="p">,</span></span><a href="#l2286"></a>
<span id="l2287">                            <span class="bp">self</span><span class="o">.</span><span class="n">_mutually_exclusive_groups</span><span class="p">)</span></span><a href="#l2287"></a>
<span id="l2288"></span><a href="#l2288"></a>
<span id="l2289">        <span class="c"># description</span></span><a href="#l2289"></a>
<span id="l2290">        <span class="n">formatter</span><span class="o">.</span><span class="n">add_text</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">description</span><span class="p">)</span></span><a href="#l2290"></a>
<span id="l2291"></span><a href="#l2291"></a>
<span id="l2292">        <span class="c"># positionals, optionals and user-defined groups</span></span><a href="#l2292"></a>
<span id="l2293">        <span class="k">for</span> <span class="n">action_group</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_action_groups</span><span class="p">:</span></span><a href="#l2293"></a>
<span id="l2294">            <span class="n">formatter</span><span class="o">.</span><span class="n">start_section</span><span class="p">(</span><span class="n">action_group</span><span class="o">.</span><span class="n">title</span><span class="p">)</span></span><a href="#l2294"></a>
<span id="l2295">            <span class="n">formatter</span><span class="o">.</span><span class="n">add_text</span><span class="p">(</span><span class="n">action_group</span><span class="o">.</span><span class="n">description</span><span class="p">)</span></span><a href="#l2295"></a>
<span id="l2296">            <span class="n">formatter</span><span class="o">.</span><span class="n">add_arguments</span><span class="p">(</span><span class="n">action_group</span><span class="o">.</span><span class="n">_group_actions</span><span class="p">)</span></span><a href="#l2296"></a>
<span id="l2297">            <span class="n">formatter</span><span class="o">.</span><span class="n">end_section</span><span class="p">()</span></span><a href="#l2297"></a>
<span id="l2298"></span><a href="#l2298"></a>
<span id="l2299">        <span class="c"># epilog</span></span><a href="#l2299"></a>
<span id="l2300">        <span class="n">formatter</span><span class="o">.</span><span class="n">add_text</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">epilog</span><span class="p">)</span></span><a href="#l2300"></a>
<span id="l2301"></span><a href="#l2301"></a>
<span id="l2302">        <span class="c"># determine help from format above</span></span><a href="#l2302"></a>
<span id="l2303">        <span class="k">return</span> <span class="n">formatter</span><span class="o">.</span><span class="n">format_help</span><span class="p">()</span></span><a href="#l2303"></a>
<span id="l2304"></span><a href="#l2304"></a>
<span id="l2305">    <span class="k">def</span> <span class="nf">format_version</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2305"></a>
<span id="l2306">        <span class="kn">import</span> <span class="nn">warnings</span></span><a href="#l2306"></a>
<span id="l2307">        <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span></span><a href="#l2307"></a>
<span id="l2308">            <span class="s">&#39;The format_version method is deprecated -- the &quot;version&quot; &#39;</span></span><a href="#l2308"></a>
<span id="l2309">            <span class="s">&#39;argument to ArgumentParser is no longer supported.&#39;</span><span class="p">,</span></span><a href="#l2309"></a>
<span id="l2310">            <span class="ne">DeprecationWarning</span><span class="p">)</span></span><a href="#l2310"></a>
<span id="l2311">        <span class="n">formatter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_formatter</span><span class="p">()</span></span><a href="#l2311"></a>
<span id="l2312">        <span class="n">formatter</span><span class="o">.</span><span class="n">add_text</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">version</span><span class="p">)</span></span><a href="#l2312"></a>
<span id="l2313">        <span class="k">return</span> <span class="n">formatter</span><span class="o">.</span><span class="n">format_help</span><span class="p">()</span></span><a href="#l2313"></a>
<span id="l2314"></span><a href="#l2314"></a>
<span id="l2315">    <span class="k">def</span> <span class="nf">_get_formatter</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2315"></a>
<span id="l2316">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">formatter_class</span><span class="p">(</span><span class="n">prog</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">prog</span><span class="p">)</span></span><a href="#l2316"></a>
<span id="l2317"></span><a href="#l2317"></a>
<span id="l2318">    <span class="c"># =====================</span></span><a href="#l2318"></a>
<span id="l2319">    <span class="c"># Help-printing methods</span></span><a href="#l2319"></a>
<span id="l2320">    <span class="c"># =====================</span></span><a href="#l2320"></a>
<span id="l2321">    <span class="k">def</span> <span class="nf">print_usage</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">file</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l2321"></a>
<span id="l2322">        <span class="k">if</span> <span class="nb">file</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2322"></a>
<span id="l2323">            <span class="nb">file</span> <span class="o">=</span> <span class="n">_sys</span><span class="o">.</span><span class="n">stdout</span></span><a href="#l2323"></a>
<span id="l2324">        <span class="bp">self</span><span class="o">.</span><span class="n">_print_message</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">format_usage</span><span class="p">(),</span> <span class="nb">file</span><span class="p">)</span></span><a href="#l2324"></a>
<span id="l2325"></span><a href="#l2325"></a>
<span id="l2326">    <span class="k">def</span> <span class="nf">print_help</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">file</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l2326"></a>
<span id="l2327">        <span class="k">if</span> <span class="nb">file</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2327"></a>
<span id="l2328">            <span class="nb">file</span> <span class="o">=</span> <span class="n">_sys</span><span class="o">.</span><span class="n">stdout</span></span><a href="#l2328"></a>
<span id="l2329">        <span class="bp">self</span><span class="o">.</span><span class="n">_print_message</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">format_help</span><span class="p">(),</span> <span class="nb">file</span><span class="p">)</span></span><a href="#l2329"></a>
<span id="l2330"></span><a href="#l2330"></a>
<span id="l2331">    <span class="k">def</span> <span class="nf">print_version</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">file</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l2331"></a>
<span id="l2332">        <span class="kn">import</span> <span class="nn">warnings</span></span><a href="#l2332"></a>
<span id="l2333">        <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span></span><a href="#l2333"></a>
<span id="l2334">            <span class="s">&#39;The print_version method is deprecated -- the &quot;version&quot; &#39;</span></span><a href="#l2334"></a>
<span id="l2335">            <span class="s">&#39;argument to ArgumentParser is no longer supported.&#39;</span><span class="p">,</span></span><a href="#l2335"></a>
<span id="l2336">            <span class="ne">DeprecationWarning</span><span class="p">)</span></span><a href="#l2336"></a>
<span id="l2337">        <span class="bp">self</span><span class="o">.</span><span class="n">_print_message</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">format_version</span><span class="p">(),</span> <span class="nb">file</span><span class="p">)</span></span><a href="#l2337"></a>
<span id="l2338"></span><a href="#l2338"></a>
<span id="l2339">    <span class="k">def</span> <span class="nf">_print_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">,</span> <span class="nb">file</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l2339"></a>
<span id="l2340">        <span class="k">if</span> <span class="n">message</span><span class="p">:</span></span><a href="#l2340"></a>
<span id="l2341">            <span class="k">if</span> <span class="nb">file</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2341"></a>
<span id="l2342">                <span class="nb">file</span> <span class="o">=</span> <span class="n">_sys</span><span class="o">.</span><span class="n">stderr</span></span><a href="#l2342"></a>
<span id="l2343">            <span class="nb">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">message</span><span class="p">)</span></span><a href="#l2343"></a>
<span id="l2344"></span><a href="#l2344"></a>
<span id="l2345">    <span class="c"># ===============</span></span><a href="#l2345"></a>
<span id="l2346">    <span class="c"># Exiting methods</span></span><a href="#l2346"></a>
<span id="l2347">    <span class="c"># ===============</span></span><a href="#l2347"></a>
<span id="l2348">    <span class="k">def</span> <span class="nf">exit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">status</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">message</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l2348"></a>
<span id="l2349">        <span class="k">if</span> <span class="n">message</span><span class="p">:</span></span><a href="#l2349"></a>
<span id="l2350">            <span class="bp">self</span><span class="o">.</span><span class="n">_print_message</span><span class="p">(</span><span class="n">message</span><span class="p">,</span> <span class="n">_sys</span><span class="o">.</span><span class="n">stderr</span><span class="p">)</span></span><a href="#l2350"></a>
<span id="l2351">        <span class="n">_sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="n">status</span><span class="p">)</span></span><a href="#l2351"></a>
<span id="l2352"></span><a href="#l2352"></a>
<span id="l2353">    <span class="k">def</span> <span class="nf">error</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">):</span></span><a href="#l2353"></a>
<span id="l2354">        <span class="sd">&quot;&quot;&quot;error(message: string)</span></span><a href="#l2354"></a>
<span id="l2355"></span><a href="#l2355"></a>
<span id="l2356"><span class="sd">        Prints a usage message incorporating the message to stderr and</span></span><a href="#l2356"></a>
<span id="l2357"><span class="sd">        exits.</span></span><a href="#l2357"></a>
<span id="l2358"></span><a href="#l2358"></a>
<span id="l2359"><span class="sd">        If you override this in a subclass, it should not return -- it</span></span><a href="#l2359"></a>
<span id="l2360"><span class="sd">        should either exit or raise an exception.</span></span><a href="#l2360"></a>
<span id="l2361"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l2361"></a>
<span id="l2362">        <span class="bp">self</span><span class="o">.</span><span class="n">print_usage</span><span class="p">(</span><span class="n">_sys</span><span class="o">.</span><span class="n">stderr</span><span class="p">)</span></span><a href="#l2362"></a>
<span id="l2363">        <span class="bp">self</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">_</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s">: error: </span><span class="si">%s</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">prog</span><span class="p">,</span> <span class="n">message</span><span class="p">))</span></span><a href="#l2363"></a></pre>
<div class="sourcelast"></div>
</div>
</div>
</div>

<script type="text/javascript">process_dates()</script>


</body>
</html>

