=======
Janelas
=======

O primeiro ponto que você deve saber é como o sistema de coordenadas do Batma funciona. Se você está vindo do XNA vai ver que possuí uma pequena diferença, o eixo y é invertido, isso pode impactar na mudança de alguns algoritmos no caso de você estar portando alguma aplicação. Se você já usa o pyglet ou cocos2d não há diferença. O canto inferior esquerdo da tela é o ponto **(0, 0)** enquanto o canto superior direito é a **(largura, altura)** - *(width, height)*.

.. image:: _static/window_coords.png
   :alt: Window coords
   :align: center
   :scale: 75%

Cada objeto :py:class:`batma.engine.Game` representa uma janela diferente e ao criar uma instancia dessa classe sem argumentos, o Batma atribuí alguns valores padrões para a configuração da janela. Os seguintes parâmetros podem ser passados como parâmetro:

**width**: *int*
    Largura da janela, em pixels. Padrão: ``640``.

**height**: *int*
    Altura da janela, em pixels. Padrão: ``480``.

**caption**: *str* ou *unicode*
    Título da janela. Padrão: ``"A Batma Game"``.

**resizable**: *bool*
    Se ``True``, o usuário poderá mudar o tamanho da janela. Padrão: ``False``.

**style**: *int*
    .

**fullscreen**: *bool*
    Se ``True``, a tela do jogo ocupará toda a tela (tela cheia). Padrão ``False``.

**visible**: *bool*
    Se ``False``, a janela não será visivel e não aparecerá na taskbar, isso é especialmente útil para criar uma tela de informação inicial até que o jogo seja carregado. Padrão ``True``.

**vsync**: *bool*
    Se ``True``, o Batma sincronizará os FPS (frames per second) com a frequência do monitor (geralmente 60hz). Padrão: ``True``.


--------
Exemplos
--------

.. code-block:: python

    game = batma.Game(width=800, height=600, caption=u'My Game')
